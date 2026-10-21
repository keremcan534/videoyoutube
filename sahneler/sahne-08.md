# Sahne 8 — İki ordu karşı karşıya

> Promptlar İngilizcedir; üreticiye İngilizce metni yapıştır. Ortak kurallar: [`stil-rehberi.md`](../stil-rehberi.md). Araç ayarları, negatif alan kuralları ve 480p test ön ayarı: [`sahne-01.md`](sahne-01.md).

## Orijinal prompt

```text
A grand panoramic view of two enormous ancient armies facing each other across a wide dry plain beneath towering distant mountains. On one side, Turkic horsemen with bows, dark lamellar armor and flowing steppe banners; on the other, disciplined ancient Near Eastern infantry with spears, shields and iron armor. Both formations hold their positions as wind drives dust between them. Slow aerial pullback emphasizing scale and tension, realistic historical epic, natural light, photorealistic, 16:9, no modern equipment, no readable text, no fantasy effects.
```

## Çekim özeti

| Alan | Değer |
|---|---|
| Süre | 8–10 sn |
| Çekim | Çok geniş, havadan panorama |
| Kamera | Yükselerek geri çekilen yavaş hava çekimi (pullback) |
| Lens | ~24 mm |
| Işık | Doğal ışık |
| Mekân | Kuru geniş ova, uzakta yüksek karlı dağlar (Sahne 1 ile aynı sıra) |
| Duygu | Gerilim, ölçek |

## Ana prompt

Veo 3.1 (Flow), Gemini Omni Flash 1.1 ve Kling 4.0 için olduğu gibi kullan. Negatif alanı olan araçlarda (Vertex Veo, Kling 3.0 Pro) son "Avoid: ..." cümlesini sil ve aşağıdaki negatif listeyi o alana koy. Runway Gen-4.5'te "Avoid" cümlesini sil; 1000 karakteri aşıyorsa anahtar kare + hareket promptu yolunu kullan.

```text
Realistic historical epic, photorealistic, 16:9 widescreen. A grand panoramic aerial view of two enormous ancient armies facing each other across a wide dry plain beneath towering distant snow-capped mountains. On the left, Turkic horsemen on compact steppe horses with recurved bows, dark lamellar armor and flowing plain steppe banners and horsetail standards; on the right, disciplined ancient Near Eastern infantry in tight ranks with long spears, round shields and iron scale armor. A wide empty strip of dry ground lies between them. Both formations hold their positions as wind drives dust across the gap. Camera: slow aerial pullback, rising away from the armies to reveal the full scale and tension, smooth and steady. Natural light, muted bronze and deep blue palette, subtle film grain. Avoid: modern equipment, readable text, fantasy effects.
```

Uzunluk: 854 karakter.

**Negatif prompt** (yalnızca negatif alanı olan araçlarda):

```text
modern equipment, vehicles, firearms, modern flags, readable text, letters, banner emblems, fantasy effects, glowing effects, magic, armies merging, soldiers walking through each other, duplicated figures, battle in progress, gore, king, ruler, crowned figure, text, subtitles, captions, letters, watermark, logo, modern objects, modern clothing, cartoon, CGI look, blurry, flicker
```

İsteğe bağlı ses satırı (ses üreten araçlarda promptun sonuna):

```text
Ambient noise: strong wind across an open plain, banners flapping, distant restless horses snorting, a low tense hush. No music, no speech.
```

## Anahtar kare (Midjourney V8.2)

Önce bu kareyi üret, sonra görselden videoya canlandır (Kling 4.0 Omni Reference/Keyframes, Runway Gen-4.5 image-to-video, Midjourney Animate). Karakter ve kalabalık sahnelerinde bu yol en tutarlı sonucu verir.

```text
grand panoramic aerial view of two enormous ancient armies facing each other across a wide dry plain beneath towering distant snow-capped mountains, on the left Turkic horsemen on compact steppe horses with recurved bows, dark lamellar armor and flowing plain steppe banners and horsetail standards, on the right disciplined ancient Near Eastern infantry in tight ranks with long spears, round shields and iron scale armor, a wide empty strip of dry ground between them, wind driving dust across the gap, natural light, muted bronze and deep blue palette, realistic historical epic, photorealistic, subtle film grain --ar 16:9 --raw --hd --no text, letters, emblem, glow
```

Hareket promptu (görselden videoya):

```text
Slow aerial pullback, the camera rising and moving away from the two armies to reveal their full scale; both formations hold perfectly still in their ranks; banners flow in the wind and dust drifts across the empty ground between them; smooth, steady camera.
```

## Bu sahneye özel kontroller

- İki ordu yerinde mi; birbirine yürüyor, karışıyor ya da savaş başlamış mı?
- Taraflar ayırt edilebiliyor mu (solda atlı Türkler, sağda piyade)?
- Kalabalık kopyala-yapıştır gibi mi görünüyor; figürler eriyor mu?
- Dağlar Sahne 1'dekiyle uyumlu mu (karlı, sarp)?
- Sancaklarda amblem/yazı ya da herhangi bir hükümdar figürü var mı?

## Notlar

- Taraflara yön verildi (Türkler solda, ordu sağda) ki model iki orduyu karıştırmasın; Sahne 6 ve 7'de de aynı yönü korumak kurguda ekseni tutarlı kılar.
- Sahne 1 ile aynı dağ sırası görünürse film baştan sona bağlanır; Sahne 1'in anahtar karesini stil referansı olarak kullanabilirsin.
- Hükümdarlar bu sahnede de gösterilmiyor; negatif listede "king, ruler, crowned figure" var.
