# Sahne 6 — Ordunun hazırlığı (hükümdar görünmüyor)

> Promptlar İngilizcedir; üreticiye İngilizce metni yapıştır. Ortak kurallar: [`stil-rehberi.md`](../stil-rehberi.md). Araç ayarları, negatif alan kuralları ve 480p test ön ayarı: [`sahne-01.md`](sahne-01.md).

## Orijinal prompt

```text
A vast ancient Near Eastern army preparing on a broad plain at sunrise, disciplined ranks of historically inspired iron-armored infantry, archers checking their bows, spearmen lifting long wooden shafts, cloth banners rippling in the wind. A royal command tent stands in the distance; the ruler himself is not shown. Slow crane shot revealing the enormous formation through morning mist, authentic material textures, cinematic scale, realistic dust and sunlight, respectful historical epic tone, 16:9, no modern flags, no readable symbols, no fantasy creatures, no visible supernatural effects.
```

## Çekim özeti

| Alan | Değer |
|---|---|
| Süre | 8–10 sn |
| Çekim | Çok geniş, ordu panoraması |
| Kamera | Sis içinden yükselerek dizilişi açan yavaş vinç çekimi |
| Lens | ~24 mm |
| Işık | Gün doğumu, sabah sisi, toz |
| Mekân | Geniş ova; uzakta kraliyet komuta çadırı |
| Duygu | Saygılı, disiplinli, görkemli |

## Ana prompt

Veo 3.1 (Flow), Gemini Omni Flash 1.1 ve Kling 4.0 için olduğu gibi kullan. Negatif alanı olan araçlarda (Vertex Veo, Kling 3.0 Pro) son "Avoid: ..." cümlesini sil ve aşağıdaki negatif listeyi o alana koy. Runway Gen-4.5'te "Avoid" cümlesini sil; 1000 karakteri aşıyorsa anahtar kare + hareket promptu yolunu kullan.

```text
Respectful historical epic tone, photorealistic, 16:9 widescreen. A vast ancient Near Eastern army prepares on a broad plain at sunrise, seen through drifting morning mist. Disciplined ranks of historically inspired infantry in iron scale armor and conical helmets over long linen tunics; archers check their bows, spearmen lift long wooden spear shafts, and plain cloth banners in solid earth colors ripple in the wind. A large royal command tent stands far in the distance with its entrance closed; no ruler or king appears anywhere in the frame. Camera: slow crane shot rising and moving forward to reveal the enormous formation, smooth and steady. Authentic textures of iron, linen, leather and wood, cinematic scale, realistic dust and low golden sunlight, natural light only, subtle film grain. Avoid: modern flags, readable symbols, fantasy creatures, supernatural effects.
```

Uzunluk: 880 karakter.

**Negatif prompt** (yalnızca negatif alanı olan araçlarda):

```text
king, ruler, crowned figure, throne, prophet, halo, modern flags, flag emblems, readable symbols, letters, fantasy creatures, jinn, giant animals, glowing effects, light beams, supernatural effects, Roman legionaries, lorica segmentata, Greek crested helmets, medieval knights, text, subtitles, captions, letters, watermark, logo, modern objects, modern clothing, cartoon, CGI look, blurry, flicker
```

İsteğe bağlı ses satırı (ses üreten araçlarda promptun sonuna):

```text
Ambient noise: wind over a wide plain, cloth banners snapping, distant clinking of armor and murmuring of a great army, footsteps on dry earth. No music, no clear speech.
```

## Anahtar kare (Midjourney V8.2)

Önce bu kareyi üret, sonra görselden videoya canlandır (Kling 4.0 Omni Reference/Keyframes, Runway Gen-4.5 image-to-video, Midjourney Animate). Karakter ve kalabalık sahnelerinde bu yol en tutarlı sonucu verir.

```text
a vast ancient Near Eastern army preparing on a broad plain at sunrise in drifting morning mist, disciplined ranks of infantry in iron scale armor and conical helmets over long linen tunics, archers checking bows, spearmen lifting long wooden spear shafts, plain cloth banners in solid earth colors rippling in the wind, a large royal command tent far in the distance with its entrance closed, high crane view, authentic iron linen leather and wood textures, realistic dust and low golden sunlight, respectful historical epic tone, photorealistic, subtle film grain --ar 16:9 --raw --hd --no king, ruler, crown, text, symbols, emblem, glow
```

Hareket promptu (görselden videoya):

```text
Slow crane shot rising and moving forward through the morning mist to reveal the enormous formation; banners ripple in the wind; archers check their bows and spearmen lift their shafts; dust drifts through the low golden sunlight; the distant command tent stays closed; smooth, steady camera.
```

## Bu sahneye özel kontroller

- Karede herhangi bir hükümdar, taçlı figür, tahta oturan kişi ya da hale var mı? Varsa klibi kullanma.
- Sancaklarda amblem, sembol ya da yazı var mı?
- Fantastik yaratık, cin, dev hayvan ya da doğaüstü ışık var mı?
- Askerler Roma lejyoneri ya da Yunan hoplitine mi benzemiş (tüylü miğfer, segmentli zırh)?
- Saflar kalabalıkta eriyor ya da tekrarlanan kopya figürler gibi mi görünüyor?

## Notlar

- Orijinaldeki "the ruler himself is not shown" en önemli kural: promptta açıkça yazıldı ve negatif listede "king, ruler, crowned figure, throne, prophet, halo" var. Hüdhüd motifi Hz. Süleyman kıssasını çağrıştırdığı için hükümdarın hiç gösterilmemesi saygı açısından da doğru.
- "Near Eastern" ordu, Turan tarafından ayırt edilsin diye demir pullu zırh, konik miğfer, uzun keten tunik ve toprak renkli düz sancaklarla tarif edildi; Roma/Yunan klişeleri negatif listede.
