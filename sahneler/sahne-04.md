# Sahne 4 — Otağda mektup

> Promptlar İngilizcedir; üreticiye İngilizce metni yapıştır. Ortak kurallar: [`stil-rehberi.md`](../stil-rehberi.md). Araç ayarları, negatif alan kuralları ve 480p test ön ayarı: [`sahne-01.md`](sahne-01.md). Karakter tanımı: [`karakterler.md`](../karakterler.md).

## Orijinal prompt

```text
Inside a vast ancient Turkic royal tent, Efrasiyab, the same mature dark-haired warrior king in dark iron lamellar armor and fur mantle, sits on a low carved throne and studies a folded parchment delivered by a hoopoe. His face shifts from curiosity to stern defiance. Oil lamps flicker, advisors stand silently in the background, slow cinematic push-in toward his expression, realistic cloth and metal textures, warm firelight against cool shadows, historically grounded epic film, 16:9, no readable text, no subtitles.
```

## Çekim özeti

| Alan | Değer |
|---|---|
| Süre | 8 sn |
| Çekim | Orta plandan yakın plana |
| Kamera | Yüzüne doğru yavaş ileri itme (push-in) |
| Lens | ~50 mm → yakın |
| Işık | Sıcak kandil ışığı, soğuk mavi gölgeler |
| Mekân | Büyük kraliyet otağının içi: kafes duvarlar, keçe ve halılar |
| Duygu | Meraktan sert bir meydan okumaya |

## Ana prompt

Veo 3.1 (Flow), Gemini Omni Flash 1.1 ve Kling 4.0 için olduğu gibi kullan. Negatif alanı olan araçlarda (Vertex Veo, Kling 3.0 Pro) son "Avoid: ..." cümlesini sil ve aşağıdaki negatif listeyi o alana koy. Runway Gen-4.5'te "Avoid" cümlesini sil; 1000 karakteri aşıyorsa anahtar kare + hareket promptu yolunu kullan.

```text
Historically grounded epic film, photorealistic, 16:9 widescreen. Inside a vast ancient Turkic royal tent of felt, its lattice walls hung with woven rugs, Efrasiyab, a mature Central Asian warrior king in his late forties, weathered sun-darkened face with high cheekbones and deep-set dark eyes, long straight dark hair worn loose past the shoulders, short dark beard, bareheaded, dark iron lamellar armor of small laced plates over a deep blue knee-length belted caftan, subtle dark fur mantle across the shoulders, leather belt with plain iron fittings, soft leather riding boots, sits on a low carved wooden throne and studies the folded parchment the hoopoe delivered, holding it so its writing faces away from the camera. His expression slowly shifts from curiosity to stern defiance. Oil lamps flicker; advisors in belted robes stand silently in the soft-focus background. Camera: slow, smooth cinematic push-in toward his face. Realistic cloth, fur and metal textures, warm firelight against cool blue shadows, muted bronze and deep blue palette, subtle film grain. Avoid: readable text, subtitles.
```

Uzunluk: 1105 karakter.

**Negatif prompt** (yalnızca negatif alanı olan araçlarda):

```text
readable text, letters, writing facing camera, runes, crown, tiara, glowing eyes, magic glow, golden throne, European castle hall, candles in chandeliers, extra fingers, distorted hands, face morphing, text, subtitles, captions, letters, watermark, logo, modern objects, modern clothing, cartoon, CGI look, blurry, flicker
```

İsteğe bağlı ses satırı (ses üreten araçlarda promptun sonuna):

```text
Ambient noise: quiet crackle of oil lamps, faint wind against the felt walls, parchment rustling. No music, no voices.
```

## Anahtar kare (Midjourney V8.2)

Önce bu kareyi üret, sonra görselden videoya canlandır (Kling 4.0 Omni Reference/Keyframes, Runway Gen-4.5 image-to-video, Midjourney Animate). Karakter ve kalabalık sahnelerinde bu yol en tutarlı sonucu verir.

```text
Efrasiyab, a mature Central Asian warrior king in his late forties, weathered sun-darkened face with high cheekbones and deep-set dark eyes, long straight dark hair worn loose past the shoulders, short dark beard, bareheaded, dark iron lamellar armor of small laced plates over a deep blue knee-length belted caftan, subtle dark fur mantle across the shoulders, leather belt with plain iron fittings, soft leather riding boots, seated on a low carved wooden throne inside a vast felt royal tent with lattice walls and woven rugs, reading a folded parchment whose back faces the viewer, stern defiant expression, oil lamps glowing, silent advisors in belted robes out of focus behind him, warm firelight against cool blue shadows, realistic cloth fur and metal textures, muted bronze and deep blue palette, photorealistic historically grounded epic film, subtle film grain --ar 16:9 --raw --hd --no text, letters, writing, crown
```

Hareket promptu (görselden videoya):

```text
Slow, smooth cinematic push-in toward the king's face; he reads the parchment and his expression shifts from curiosity to stern defiance, his jaw tightening; oil lamp flames flicker gently; advisors stay still in the background; warm firelight against cool shadows.
```

## Bu sahneye özel kontroller

- Parşömenin yazılı yüzü kameraya dönük mü; okunabilir harf var mı?
- İfade değişimi doğal mı, yoksa yüz başka birine mi dönüşüyor?
- Efrasiyab 2. sahnedekiyle aynı mı (saç, sakal, zırh, kaftan rengi)?
- Taç ya da altın taht çıkmış mı?
- Kandil alevleri gerçekçi mi; ışık titremesi tüm kareyi mi titretiyor?

## Notlar

- Orijinaldeki "delivered by a hoopoe" korundu; model hüdhüdü sahneye ekleyebilir. Süreklilik için bu iyi olabilir (ör. direkte ya da bir sırıkta tünemiş). İstemiyorsan o ifadeyi "the folded parchment message" yap.
- İfade değişimi (meraktan meydan okumaya) yüz kaymasına en açık an; karakter referans görseliyle görselden videoya git.
- Kemer, kaftan ve zırh tanımı `karakterler.md`'den kelimesi kelimesine alındı.
