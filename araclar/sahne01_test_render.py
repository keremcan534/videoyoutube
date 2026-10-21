#!/usr/bin/env python3
"""Sahne 1 için hızlı, prosedürel test videosu (animatik).

Yapay zekâ video üreticisinin yerine geçmez: kompozisyonu, kamera hareketini,
zamanlamayı ve renk paletini düşük çözünürlükte hızlıca görmek içindir.
Sadece numpy, Pillow ve ffmpeg gerekir.

    python3 araclar/sahne01_test_render.py                       # 854x480, 24 fps, 8 sn
    python3 araclar/sahne01_test_render.py --stills onizleme/kareler --only-stills
"""
import argparse
import multiprocessing
import os
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

LUMA = np.array([0.2126, 0.7152, 0.0722], np.float32)


def hexcol(h):
    h = h.lstrip('#')
    return np.array([int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)], np.float32)


def smoothstep(e0, e1, x):
    t = np.clip((x - e0) / (e1 - e0), 0, 1)
    return t * t * (3 - 2 * t)


def lerp(a, b, t):
    return a + (b - a) * t


def fractal_2d(rng, n, slope):
    """Döşenebilir fBm dokusu (spektral sentez), [0, 1] aralığında."""
    f = np.fft.fftfreq(n)
    r = np.sqrt(f[:, None] ** 2 + f[None, :] ** 2)
    r[0, 0] = 1
    spec = np.fft.fft2(rng.standard_normal((n, n))) / r ** slope
    spec[0, 0] = 0
    t = np.real(np.fft.ifft2(spec))
    lo, hi = np.percentile(t, [1, 99])
    return np.clip((t - lo) / (hi - lo), 0, 1).astype(np.float32)


def fractal_1d(rng, n, slope):
    f = np.fft.rfftfreq(n)
    f[0] = 1
    spec = np.fft.rfft(rng.standard_normal(n)) / f ** slope
    spec[0] = 0
    t = np.fft.irfft(spec, n)
    return (t / np.abs(t).max()).astype(np.float32)


def mip_pyramid(tex):
    levels = [tex]
    while levels[-1].shape[0] > 4:
        t = levels[-1]
        levels.append(0.25 * (t[0::2, 0::2] + t[1::2, 0::2] + t[0::2, 1::2] + t[1::2, 1::2]))
    return levels


def sample_wrap(tex, u, v):
    """Döşenebilir dokudan bilineer örnekleme (u, v doku pikseli cinsinden)."""
    n = tex.shape[0]
    u0 = np.floor(u)
    v0 = np.floor(v)
    fu = (u - u0).astype(np.float32)
    fv = (v - v0).astype(np.float32)
    u0 = u0.astype(np.int64) % n
    v0 = v0.astype(np.int64) % n
    u1 = (u0 + 1) % n
    v1 = (v0 + 1) % n
    top = lerp(tex[v0, u0], tex[v0, u1], fu)
    bot = lerp(tex[v1, u0], tex[v1, u1], fu)
    return lerp(top, bot, fv)


def sample_mip(pyr, u, v, lod):
    """Trilineer örnekleme: uzaktaki perspektif yüzeylerde titremeyi önler."""
    lod = np.clip(lod, 0, len(pyr) - 1.001)
    l0 = np.floor(lod).astype(np.int64)
    t = (lod - l0).astype(np.float32)
    out = np.empty(u.shape, np.float32)
    for level in np.unique(l0):
        m = l0 == level
        s0, s1 = 2.0 ** level, 2.0 ** (level + 1)
        a = sample_wrap(pyr[level], (u[m] + 0.5) / s0 - 0.5, (v[m] + 0.5) / s0 - 0.5)
        b = sample_wrap(pyr[level + 1], (u[m] + 0.5) / s1 - 0.5, (v[m] + 0.5) / s1 - 0.5)
        out[m] = lerp(a, b, t[m])
    return out


def box_blur(a, r, axis):
    r = max(1, int(round(r)))
    pad = [(0, 0)] * a.ndim
    pad[axis] = (r + 1, r)
    c = np.cumsum(np.pad(a, pad, mode='edge'), axis=axis, dtype=np.float32)
    n = a.shape[axis]
    hi = np.take(c, np.arange(2 * r + 1, 2 * r + 1 + n), axis=axis)
    lo = np.take(c, np.arange(n), axis=axis)
    return (hi - lo) / (2 * r + 1)


def blur(a, radius):
    # Üç kez kutu bulanıklığı ~ Gauss bulanıklığı
    r = radius / 1.7
    for _ in range(3):
        a = box_blur(box_blur(a, r, 0), r, 1)
    return a


def gradient(v, stops):
    pos = np.array([p for p, _ in stops], np.float32)
    cols = np.stack([hexcol(c) for _, c in stops])
    return np.stack([np.interp(v, pos, cols[:, i]) for i in range(3)], axis=-1).astype(np.float32)


def draw_rider(d, ox, oy, s, phase, kind, sway):
    """Sağa doğru giden atlı silueti. Birim: 0,1 m; (ox, oy) atın altındaki zemin noktası."""
    bob = 0.35 * np.sin(2 * phase)

    def P(x, y):
        return (ox + x * s, oy + y * s)

    w = max(1, int(round(1.3 * s)))
    # Bacaklar: tırıs, çapraz çiftler birlikte hareket eder
    for hx, off in ((-5.5, 0.0), (-4.5, np.pi), (5.0, np.pi), (6.0, 0.0)):
        a = 0.45 * np.sin(phase + off)
        lift = max(0.0, np.sin(phase + off + np.pi / 2)) * 1.4
        top = (hx, -9 + bob)
        knee = (hx + 4 * np.sin(a), -9 + bob + 4.4 * np.cos(a))
        foot = (knee[0] + 3.6 * np.sin(0.6 * a - 0.15), -lift)
        d.line([P(*top), P(*knee), P(*foot)], fill=255, width=w)
    d.ellipse([P(-8, -14 + bob), P(8, -7.5 + bob)], fill=255)
    d.polygon([P(5.5, -13 + bob), P(8.5, -19 + bob), P(11, -19.5 + bob), P(14.5, -15.5 + bob),
               P(13.5, -14.3 + bob), P(10, -16 + bob), P(8, -10 + bob)], fill=255)
    d.polygon([P(9.4, -19.3 + bob), P(10, -21.6 + bob), P(10.8, -19.4 + bob)], fill=255)
    d.line([P(-7.5, -12.5 + bob), P(-10.5, -8 + 0.8 * np.sin(phase)), P(-10, -4.5)], fill=255, width=w)
    # Binici: keçe başlık, sırtta yay kılıfı
    d.line([P(-0.5, -14 + bob), P(1.5, -10.5 + bob), P(0.8, -8.5 + bob)], fill=255, width=w)
    d.polygon([P(-2.2, -13.5 + bob), P(1.6, -13.5 + bob), P(1.9, -21.5 + bob), P(-1.4, -21.5 + bob)], fill=255)
    d.ellipse([P(-1.5, -25.4 + bob), P(2.1, -21.8 + bob)], fill=255)
    d.polygon([P(-1.7, -24.4 + bob), P(0.5, -27.6 + bob), P(2.2, -24.4 + bob)], fill=255)
    d.line([P(1.0, -20.5 + bob), P(4.8, -16.5 + bob)], fill=255, width=w)
    d.line([P(-2.0, -20.5 + bob), P(-3.6, -14.5 + bob)], fill=255, width=w)
    if kind in ('mizrak', 'tug'):
        d.line([P(1.4, -12 + bob), P(-2.6, -40 + bob)], fill=255, width=max(1, int(round(0.7 * s))))
    if kind == 'tug':
        # At kılı tuğ: rüzgârla sallanan kıllar + küçük flama
        for j in range(4):
            d.line([P(-2.6, -39 + bob), P(-4.2 - j * 0.6 - sway, -33 + j * 0.4 + bob)], fill=255,
                   width=max(1, int(round(0.6 * s))))
        d.polygon([P(-2.5, -40 + bob), P(-8 - sway, -38.6 + bob), P(-2.4, -37.4 + bob)], fill=255)


class Sahne:
    def __init__(self, W, H, seed=7):
        self.W, self.H = W, H
        self.k = H / 480  # 480p'ye göre ölçek
        rng = np.random.default_rng(seed)
        self.cx = W / 2
        self.yh = 0.58 * H  # ufuk çizgisi
        self.f = (W / 2) / np.tan(np.radians(30))  # 60° yatay görüş açısı
        self.cam_h = 12.0  # m, alçak drone yüksekliği
        self.cam_speed = 5.0  # m/sn, yavaş ileri itme
        self.xs = 0.62 * W  # güneşin yatay konumu
        ys, xs = np.mgrid[0:H, 0:W].astype(np.float64)
        self.X, self.Y = xs + 0.5, ys + 0.5
        self.sunprox = np.exp(-((self.X - self.xs) / (0.38 * W)) ** 2).astype(np.float32)

        self.grass = mip_pyramid(fractal_2d(rng, 1024, 0.9))
        self.patch = mip_pyramid(fractal_2d(rng, 512, 1.3))
        self.cloud = mip_pyramid(fractal_2d(rng, 1024, 1.15))
        self.rock = fractal_2d(rng, 512, 1.0)

        # Dağ sıraları: ufkun üstündeki yükseklik (480p pikseli), x = [0, 1].
        # Arkadan aydınlatılmış, pusla ayrışan katmanlar; güneş x = 0,62'deki boyundan doğar.
        n = 4096
        self.xn = np.linspace(0, 1, n)
        x = self.xn

        def sira(base, peaks, rug, dip):
            h = base + sum(a * np.exp(-np.abs((x - c) / w) ** 1.3) for c, a, w in peaks)
            detail = 0.75 * fractal_1d(rng, n, 1.1) + 0.25 * (1 - 2 * np.abs(fractal_1d(rng, n, 0.95)))
            h = h + rug * detail * (0.5 + 0.5 * h / h.max())
            return h - dip * np.exp(-((x - 0.62) / 0.07) ** 2)

        def yumusak_min(a, b, s=6.0):
            hmix = np.clip(0.5 + 0.5 * (b - a) / s, 0, 1)
            return lerp(b, a, hmix) - s * hmix * (1 - hmix)

        far = sira(70, [(0.08, 80, 0.06), (0.27, 105, 0.07), (0.43, 70, 0.05), (0.79, 95, 0.06),
                        (0.95, 75, 0.05)], 34, 38)
        h_sun = np.interp(0.62, x, far)
        # Öndeki sıralar güneşi kapatmasın: pürüzlü, yumuşak bir tavan
        cap = h_sun * 0.72 + 2600 * (x - 0.62) ** 2

        def tavan(scale):
            return cap * scale + 5 * scale * fractal_1d(rng, n, 1.0)

        ridges = [
            yumusak_min(sira(40, [(0.16, 60, 0.07), (0.36, 45, 0.06), (0.70, 55, 0.07), (0.90, 40, 0.05)], 22, 26),
                        tavan(1.0)),
            yumusak_min(sira(20, [(0.05, 30, 0.08), (0.48, 26, 0.08), (0.84, 34, 0.07)], 14, 14), tavan(0.75)),
            yumusak_min(sira(7, [(0.22, 18, 0.10), (0.55, 10, 0.08), (0.93, 22, 0.08)], 7, 5), tavan(0.45)),
        ]
        # (profil, yakınlaşma hızı, koyu, açık, sis tabanı, sis artışı, kenar ışığı, kar)
        self.layers = [
            (far, 0.025, '#495270', '#3f4762', 0.30, 0.50, 0.9, True),
            (ridges[0], 0.03, '#3b435b', '#343b51', 0.22, 0.50, 0.7, False),
            (ridges[1], 0.04, '#2d3345', '#282d3d', 0.14, 0.50, 0.55, False),
            (ridges[2], 0.055, '#24272f', '#1e2128', 0.08, 0.45, 0.4, False),
        ]

        # Atlı kolu: dünya koordinatları (m)
        self.riders = []
        for i in range(11):
            kind = 'tug' if i == 0 else ('mizrak' if i % 3 == 0 else 'yay')
            self.riders.append(dict(x0=-5.2 * i + rng.uniform(-0.8, 0.8), z=400 + rng.uniform(-14, 14),
                                    phase=rng.uniform(0, 2 * np.pi), kind=kind))
        self.vignette = (1 - 0.30 * np.clip(np.hypot((self.X - self.cx) / (0.5 * W),
                                                       (self.Y - H / 2) / (0.5 * W)) ** 2.2, 0, 1)
                         ).astype(np.float32)[..., None]

    def ridge(self, profile, zoom):
        xw = self.cx + (self.X[0] - self.cx) / zoom
        h = np.interp(xw / self.W, self.xn, profile) * self.k
        return self.yh - h * zoom, h * zoom, xw

    def frame(self, t, T, rng):
        W, H, k, yh, f = self.W, self.H, self.k, self.yh, self.f
        X, Y, sp = self.X, self.Y, self.sunprox
        u = t / T
        cam_z = self.cam_speed * t

        # Gökyüzü
        img = gradient(np.clip(Y / yh, 0, 1), [(0, '#1a2640'), (0.45, '#2b3958'), (0.72, '#4f4e62'),
                                                (0.88, '#93694f'), (1.0, '#d79d5e')])
        far_top, _, _ = self.ridge(self.layers[0][0], 1 + self.layers[0][1] * u)
        sx = int(round(self.xs))
        sun_y = far_top[sx] - (2 + 5 * u) * k  # güneş dağ boynundan yavaşça yükselir
        r = np.hypot(X - self.xs, Y - sun_y)
        glow = 0.45 * np.exp(-(r / (38 * k)) ** 2) + 0.28 * np.exp(-r / (140 * k))
        glow += 0.22 * np.exp(-((Y - yh) / (34 * k)) ** 2) * sp
        img += glow[..., None].astype(np.float32) * hexcol('#ffbf73')
        disc = smoothstep(6.0 * k, 4.8 * k, r)[..., None].astype(np.float32)
        img = lerp(img, np.float32(2.6) * hexcol('#fff0cc'), disc)

        # Fırtına bulutları: perspektifli bulut tabanı; tepede ağır, gün doğumunun üstünde
        # yırtık; zamanla yoğunlaşır ve kamera ilerledikçe üstümüzden akar.
        cm = Y < 0.47 * H
        dyc = np.maximum(yh - Y[cm], 0.5)
        zc = 2000.0 * f / dyc
        cxw = (X[cm] - self.cx) * zc / f + 30.0 * t
        czw = zc + cam_z * 3
        lod = np.log2(np.maximum(np.maximum(zc / f, zc * zc / (2000.0 * f)) / 150.0, 1e-6))
        c = sample_mip(self.cloud, cxw / 150, czw / 150, lod)
        c_sun = sample_mip(self.cloud, cxw / 150, (czw + 900) / 150, lod)
        detail = sample_mip(self.cloud, cxw / 45 + 500, czw / 45, lod + np.log2(150 / 45))
        yc = Y[cm].astype(np.float32)
        bias = 0.55 * (1 - smoothstep(0.0, 0.40 * H, yc)) ** 1.2
        th = 0.50 - 0.10 * u
        dens = smoothstep(th, th + 0.24, c + bias + 0.14 * (detail - 0.5))
        lit = smoothstep(0.0, 0.14, c - c_sun)
        under = smoothstep(0.15 * H, 0.42 * H, yc)
        spc = sp[cm]
        shade = np.clip(0.55 * detail + 0.45 * c - 0.15, 0, 1) ** 1.4
        ccol = lerp(hexcol('#0d1019'), hexcol('#4a4f61'), shade[:, None])
        ccol += ((0.7 * lit + 0.5 * under) * (0.2 + 0.8 * spc) * (0.25 + 0.75 * (1 - dens)))[:, None] \
            * hexcol('#d48e52')
        alpha = (dens * (1 - smoothstep(0.30 * H, 0.45 * H, yc)) * 0.98).astype(np.float32)
        img[cm] = lerp(img[cm], ccol, alpha[:, None])

        # Dağlar: arkadan aydınlatılmış, pusla ayrışan sıralar; en uzaktakinin zirveleri karlı
        haze = lerp(hexcol('#7b7280'), hexcol('#e2ab6a'), sp[..., None])
        for prof, zr, dark, light, fog0, fogk, rimk, snow in self.layers:
            zoom = 1 + zr * u
            top, hgt, xw = self.ridge(prof, zoom)
            m = (Y + 0.5 > top[None, :]) & (Y < yh + 3 * k)
            cov = np.clip(Y + 0.5 - top[None, :], 0, 1)[m].astype(np.float32)
            d = (Y - top[None, :])[m]
            hh = np.broadcast_to(hgt[None, :], Y.shape)[m]
            rel = np.clip(d / np.maximum(hh, 1), 0, 1)
            xm = np.broadcast_to(xw[None, :], Y.shape)[m] / k
            ym = ((Y[m] - yh) / zoom) / k
            tex = sample_wrap(self.rock, xm * 0.9, ym * 0.9)
            gully = sample_wrap(self.rock, xm * 2.2 + 200, ym * 0.6)
            col = lerp(hexcol(dark), hexcol(light), (0.6 * tex + 0.4 * gully)[:, None])
            if snow:
                h480 = hh / (zoom * k)
                depth = np.clip(h480 - 95, 0, None) * 0.7 * k * zoom + (gully - 0.5) * 16 * k
                snowm = (smoothstep(-1.5 * k, 1.5 * k, depth - d) * smoothstep(85, 110, h480)).astype(np.float32)
                col = lerp(col, lerp(hexcol('#626c86'), hexcol('#7d86a0'), tex[:, None]), snowm[:, None] * 0.85)
            spm = sp[m]
            fog = np.clip(fog0 + fogk * rel ** 1.4 + 0.22 * spm, 0, 0.93).astype(np.float32)
            col = lerp(col, haze[m], fog[:, None])
            rim = (np.exp(-d / (1.1 * k)) * (0.2 + 0.8 * spm) * rimk).astype(np.float32)
            col += rim[:, None] * hexcol('#ffc884')
            img[m] = lerp(img[m], col, cov[:, None])

        # Bozkır: perspektifli zemin; tümsek gölgeleri, rüzgâr dalgaları, bulut gölgeleri
        gm = Y > yh
        z = self.cam_h * f / (Y[gm] - yh)
        gx = (X[gm] - self.cx) * z / f
        gz = z + cam_z
        lat, dep = z / f, z * z / (self.cam_h * f)
        fp = np.maximum(lat, dep) * 0.7
        clump = sample_mip(self.grass, gx / 0.5, gz / 0.5, np.log2(fp / 0.5))
        patch = sample_mip(self.patch, gx / 4, gz / 4, np.log2(fp / 4))
        region = sample_mip(self.patch, gx / 30 + 300, gz / 30 + 300, np.log2(fp / 30))
        region2 = sample_mip(self.patch, gx / 30 + 300, (gz + 25) / 30 + 300, np.log2(fp / 30))
        g = smoothstep(0.15, 0.85, 0.35 * clump + 0.4 * patch + 0.25 * region)
        col = lerp(hexcol('#4a3720'), hexcol('#c29752'), g[:, None])
        col = lerp(col, col * hexcol('#bdbf8e'), smoothstep(0.5, 0.75, region)[:, None] * 0.55)
        # Arazi tümsekleri: güneşe (ileriye) bakan yamaçlar aydınlık
        slope = np.clip(0.5 - (region2 - region) * 9, 0, 1)
        wdir = gx * 0.55 + gz * 0.83
        wave = np.sin(2 * np.pi * (wdir - 6.5 * t) / 18 + 3 * patch)
        gust = smoothstep(0.3, 0.7, sample_mip(self.patch, (gx - 4 * t) / 35, (gz - 5.5 * t) / 35, np.log2(fp / 35)))
        fpw = np.hypot(0.55 * lat, 0.83 * dep)
        sheen = np.clip(wave, 0, 1) ** 1.5 * gust * np.clip(1 - fpw / 4.5, 0, 1)
        shadow = smoothstep(0.5, 0.7, sample_mip(self.cloud, (gx + 30 * t) / 60, (gz + 3 * cam_z) / 60,
                                                   np.log2(fp / 60)))
        light = lerp(0.55, 1.0, smoothstep(50, 1000, z)) * (1 - 0.35 * shadow) * (0.7 + 0.6 * slope)
        spg = sp[gm]
        back = spg * smoothstep(60, 1500, z) * 0.55 + 0.1
        col = col * light[:, None] + (back * (0.5 + 0.5 * g) * (0.7 + 0.6 * slope))[:, None] * 0.5 * hexcol('#ffbd6e')
        col += (sheen * (0.45 + 0.55 * light) * 0.28)[:, None] * hexcol('#ffd49a')
        fog = (1 - np.exp(-z / 2400)).astype(np.float32)
        img[gm] = lerp(col.astype(np.float32), haze[gm], fog[:, None])

        # Vadi pusu
        mist = (np.exp(-((Y - (yh - 6 * k)) / (10 * k)) ** 2) * (0.30 + 0.40 * sp)).astype(np.float32)
        img = lerp(img, haze * 1.08, mist[..., None])

        img = self.horsemen(img, t, haze)

        # Parlama (bloom), ton eğrisi, renk derecelendirme, vinyet, film greni
        bright = np.clip(img - 0.72, 0, None)
        img = img + (0.55 * blur(bright, 6 * k) + 0.45 * blur(bright, 26 * k)) * hexcol('#ffd2a0')
        img = np.where(img < 0.8, img, 0.8 + 0.2 * (1 - np.exp(-(img - 0.8) / 0.2)))
        lum = (img @ LUMA)[..., None]
        img = lerp(lum, img, 0.85)
        sh = 1 - smoothstep(0.0, 0.45, lum)
        hl = smoothstep(0.45, 1.0, lum)
        img = lerp(img, hexcol('#1d2c4a') + 0.6 * lum, 0.22 * sh)
        img = lerp(img, img * hexcol('#ffdcae') * 1.06, 0.35 * hl)
        img = lerp(img, img * img * (3 - 2 * img), 0.3)
        img = img * self.vignette
        lum = (img @ LUMA)[..., None]
        img += rng.normal(0, 0.018, (H, W, 1)).astype(np.float32) * (0.6 + 0.4 * (1 - lum))
        img += rng.normal(0, 0.005, (H, W, 3)).astype(np.float32)
        return (np.clip(img, 0, 1) * 255 + 0.5).astype(np.uint8)

    def horsemen(self, img, t, haze):
        W, k, f, yh = self.W, self.k, self.f, self.yh
        cam_z = self.cam_speed * t
        y0 = int(yh - 30 * k)
        y1 = int(yh + 45 * k)
        ss = 4  # süper örnekleme
        canvas = Image.new('L', (W * ss, (y1 - y0) * ss), 0)
        d = ImageDraw.Draw(canvas)
        band = img[y0:y1]
        dust = np.zeros(band.shape[:2], np.float32)
        by, bx = np.mgrid[y0:y1, 0:W].astype(np.float32) + 0.5
        for rd in self.riders:
            zc = rd['z'] - cam_z
            wx = rd['x0'] + 4.0 * t  # tırıs, ~4 m/sn
            x = self.cx + wx * f / zc
            y = yh + self.cam_h * f / zc
            s = 0.1 * f / zc * 2.3  # görünürlük için abartılı ölçek
            phase = rd['phase'] + 2 * np.pi * t / 0.55
            for j in range(1, 6):
                dx, dyy, rad = x - (2 + 3.2 * j) * k, y - (1 + 0.6 * j) * k, (1.6 + 1.1 * j) * k
                dust += 0.09 * (1 - j / 6) * np.exp(-((bx - dx) ** 2 + (by - dyy) ** 2) / (2 * rad * rad))
            draw_rider(d, x * ss, (y - y0) * ss, s * ss, phase, rd['kind'], 1.2 * np.sin(2.1 * t + rd['phase']))
        mask = np.asarray(canvas.resize((W, y1 - y0), Image.BOX), np.float32)[..., None] / 255
        hz = haze[y0:y1]
        band = lerp(band, hz * 1.05, np.clip(dust, 0, 0.35)[..., None])
        band = lerp(band, lerp(hexcol('#15110d'), hz, 0.16), mask)
        img[y0:y1] = band
        return img


_IS = {}  # fork ile işçi süreçlere aktarılan sahne ve zamanlama


def _kare(i):
    s = _IS
    return s['sahne'].frame(i / s['fps'], s['T'], np.random.default_rng(s['seed'] * 100003 + i)).tobytes()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--width', type=int, default=854)
    ap.add_argument('--height', type=int, default=480)
    ap.add_argument('--fps', type=int, default=24)
    ap.add_argument('--seconds', type=float, default=8.0)
    ap.add_argument('--seed', type=int, default=7)
    ap.add_argument('--crf', type=int, default=23)
    ap.add_argument('--jobs', type=int, default=os.cpu_count() or 1, help='paralel kare sayısı')
    ap.add_argument('--out', default='onizleme/sahne-01-test-480p24.mp4')
    ap.add_argument('--stills', help='başlangıç, orta ve son kareyi PNG olarak bu klasöre yaz')
    ap.add_argument('--only-stills', action='store_true', help='video üretmeden sadece kareleri yaz')
    a = ap.parse_args()
    if a.width % 2 or a.height % 2:
        sys.exit('genişlik ve yükseklik çift sayı olmalı (yuv420p)')

    n = int(round(a.seconds * a.fps))
    _IS.update(sahne=Sahne(a.width, a.height, a.seed), fps=a.fps, T=n / a.fps, seed=a.seed)

    if a.stills:
        Path(a.stills).mkdir(parents=True, exist_ok=True)
        for i in sorted({0, n // 2, n - 1}):
            frame = np.frombuffer(_kare(i), np.uint8).reshape(a.height, a.width, 3)
            Image.fromarray(frame).save(Path(a.stills) / f'kare-{i:03d}.png')
        if a.only_stills:
            return

    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
           '-s', f'{a.width}x{a.height}', '-r', str(a.fps), '-i', '-',
           '-c:v', 'libx264', '-preset', 'medium', '-crf', str(a.crf), '-pix_fmt', 'yuv420p',
           '-movflags', '+faststart', a.out]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    with multiprocessing.get_context('fork').Pool(max(1, a.jobs)) as pool:
        for i, frame in enumerate(pool.imap(_kare, range(n), chunksize=2)):
            proc.stdin.write(frame)
            if (i + 1) % a.fps == 0:
                print(f'{i + 1}/{n} kare', file=sys.stderr)
    proc.stdin.close()
    if proc.wait():
        sys.exit('ffmpeg hata verdi')
    print(a.out)


if __name__ == '__main__':
    main()
