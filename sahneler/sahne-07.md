# Sahne 7 — Savaş davulları ve and

> Promptlar İngilizcedir; üreticiye İngilizce metni yapıştır. Ortak kurallar: [`stil-rehberi.md`](../stil-rehberi.md). Araç ayarları, negatif alan kuralları ve 480p test ön ayarı: [`sahne-01.md`](sahne-01.md).

## Orijinal prompt

```text
Low-angle cinematic shot of ancient Turkic warriors beating large hide-covered war drums and sounding long curved horns before battle. Rows of powerful horses stamp the dry earth, dust rises around their legs, banners snap in strong wind, warriors lift their weapons in a solemn battle oath. Camera slowly tracks across the line, realistic horse anatomy and grounded ancient equipment, thunderous atmosphere suggested by movement and dust, photorealistic historical epic, 16:9, no gore, no text.
```

## Çekim özeti

| Alan | Değer |
|---|---|
| Süre | 8 sn |
| Çekim | Alçak açı, orta-geniş |
| Kamera | Saf boyunca yavaş yanal takip |
| Lens | ~35 mm |
| Işık | Kapalı hava, tozla yumuşamış ışık |
| Mekân | Kuru bozkır, savaş öncesi saf |
| Duygu | Ağırbaşlı yemin, gök gürültüsü gibi atmosfer |

## Ana prompt

Veo 3.1 (Flow), Gemini Omni Flash 1.1 ve Kling 4.0 için olduğu gibi kullan. Negatif alanı olan araçlarda (Vertex Veo, Kling 3.0 Pro) son "Avoid: ..." cümlesini sil ve aşağıdaki negatif listeyi o alana koy. Runway Gen-4.5'te "Avoid" cümlesini sil; 1000 karakteri aşıyorsa anahtar kare + hareket promptu yolunu kullan.

```text
Photorealistic historical epic, 16:9 widescreen. Low-angle cinematic shot of ancient Turkic warriors before battle: drummers beat large hide-covered kettle war drums with wooden sticks, and warriors sound long curved horns. Behind them, rows of powerful compact steppe horses stamp the dry earth, dust rising around their legs, and plain steppe banners and horsetail standards snap in strong wind. The warriors, in dark lamellar armor and belted caftans, lift their spears and recurved bows together in a solemn battle oath. Camera: slow, steady low-angle tracking shot across the line from left to right. Realistic horse anatomy and grounded ancient equipment, a thunderous atmosphere suggested by movement and dust, overcast light, muted bronze and deep blue palette, subtle film grain. Avoid: gore, text.
```

Uzunluk: 807 karakter.

**Negatif prompt** (yalnızca negatif alanı olan araçlarda):

```text
gore, blood, wounds, text, letters, banner emblems, modern drums, drum kit, brass trumpets, extra legs, morphing horses, merged horses, distorted hands, fantasy armor, horned helmets, glowing effects, text, subtitles, captions, letters, watermark, logo, modern objects, modern clothing, cartoon, CGI look, blurry, flicker
```

İsteğe bağlı ses satırı (ses üreten araçlarda promptun sonuna):

```text
Sound design: deep booming war drums in a slow steady rhythm, long low horn calls, hooves stamping dry earth, banners snapping in strong wind. No music other than the drums and horns, no speech.
```

## Anahtar kare (Midjourney V8.2)

Önce bu kareyi üret, sonra görselden videoya canlandır (Kling 4.0 Omni Reference/Keyframes, Runway Gen-4.5 image-to-video, Midjourney Animate). Karakter ve kalabalık sahnelerinde bu yol en tutarlı sonucu verir.

```text
low-angle view of ancient Turkic warriors before battle beating large hide-covered kettle war drums and sounding long curved horns, rows of powerful compact steppe horses stamping the dry earth with dust rising around their legs, plain steppe banners and horsetail standards snapping in strong wind, warriors in dark lamellar armor and belted caftans lifting spears and recurved bows in a solemn battle oath, overcast light, realistic horse anatomy, grounded ancient equipment, muted bronze and deep blue palette, photorealistic historical epic, subtle film grain --ar 16:9 --raw --hd --no text, letters, blood, emblem
```

Hareket promptu (görselden videoya):

```text
Slow, steady low-angle tracking shot across the line from left to right; drummers strike the war drums in a steady rhythm and horn players raise long curved horns; horses stamp and dust rises around their legs; banners snap in the strong wind; warriors lift their weapons together in a solemn oath.
```

## Bu sahneye özel kontroller

- Kan, yara ya da şiddet görüntüsü var mı?
- Davullar deri kaplı büyük kös davulu mu; modern davul seti ya da pirinç trompet çıkmış mı?
- Atlarda fazla/eksik bacak, birbirine kaynaşma var mı?
- Sancaklarda amblem ya da yazı var mı?
- Davul vuruşları ve el hareketleri tutarlı mı (sopa elden kayboluyor mu)?

## Notlar

- Veo, Kling ve Omni bu sahnede davul ve borazan sesini de üretebilir; ses satırı bu yüzden önemli. Runway sessiz; sesi ayrıca ekle.
- "Long curved horns" Türk geleneğindeki boru/borazan için; modeller bazen hayvan boynuzu çıkarıyor, bu da uygun.
