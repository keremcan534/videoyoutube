# Sahne 5 — Savaş meclisi

> Promptlar İngilizcedir; üreticiye İngilizce metni yapıştır. Ortak kurallar: [`stil-rehberi.md`](../stil-rehberi.md). Araç ayarları, negatif alan kuralları ve 480p test ön ayarı: [`sahne-01.md`](sahne-01.md). Karakter tanımı: [`karakterler.md`](../karakterler.md).

## Orijinal prompt

```text
Inside an ancient Central Asian Turkic war council tent, Efrasiyab stands over a rough leather map with several seasoned commanders. One commander points toward the distant horizon. Warriors tighten leather straps, inspect iron helmets and prepare bows. Firelight flickers across determined faces, slow lateral camera movement, realistic historically inspired equipment, grounded premodern military atmosphere, tense silence, cinematic photorealism, 16:9, no modern maps, no readable text, no fantasy armor.
```

## Çekim özeti

| Alan | Değer |
|---|---|
| Süre | 8 sn |
| Çekim | Orta-geniş grup çekimi |
| Kamera | Soldan sağa yavaş yanal kaydırma |
| Lens | ~35 mm |
| Işık | Mangal ve kandil ateşi, titrek |
| Mekân | Savaş meclisi çadırı; açık kapıdan uzak ufuk |
| Duygu | Gergin sessizlik, kararlılık |

## Ana prompt

Veo 3.1 (Flow), Gemini Omni Flash 1.1 ve Kling 4.0 için olduğu gibi kullan. Negatif alanı olan araçlarda (Vertex Veo, Kling 3.0 Pro) son "Avoid: ..." cümlesini sil ve aşağıdaki negatif listeyi o alana koy. Runway Gen-4.5'te "Avoid" cümlesini sil; 1000 karakteri aşıyorsa anahtar kare + hareket promptu yolunu kullan.

```text
Cinematic photorealism, 16:9 widescreen. Inside an ancient Central Asian Turkic war council tent, Efrasiyab, a mature Central Asian warrior king in his late forties, weathered sun-darkened face with high cheekbones and deep-set dark eyes, long straight dark hair worn loose past the shoulders, short dark beard, bareheaded, dark iron lamellar armor of small laced plates over a deep blue knee-length belted caftan, subtle dark fur mantle across the shoulders, leather belt with plain iron fittings, soft leather riding boots, stands over a rough leather map spread on a low wooden table, surrounded by several seasoned commanders in dark lamellar armor and belted caftans. One commander points toward the distant horizon through the open tent flap. Around them, warriors tighten leather straps, inspect conical iron helmets and string recurved composite bows. Firelight from braziers flickers across determined faces. Camera: slow, smooth lateral movement from left to right. Realistic historically inspired equipment, grounded premodern military atmosphere, tense silence, muted bronze and deep blue palette, subtle film grain. The map shows only rough painted rivers and mountains. Avoid: modern maps, readable text, fantasy armor.
```

Uzunluk: 1233 karakter.

**Negatif prompt** (yalnızca negatif alanı olan araçlarda):

```text
modern map, printed map, compass rose, grid lines, readable text, letters, labels, fantasy armor, spiked armor, horned helmets, plate armor, glowing weapons, crown, extra fingers, distorted hands, face morphing, text, subtitles, captions, letters, watermark, logo, modern objects, modern clothing, cartoon, CGI look, blurry, flicker
```

İsteğe bağlı ses satırı (ses üreten araçlarda promptun sonuna):

```text
Ambient noise: crackling braziers, leather creaking, metal plates clinking softly, wind outside the tent. No music, no speech.
```

## Anahtar kare (Midjourney V8.2)

Önce bu kareyi üret, sonra görselden videoya canlandır (Kling 4.0 Omni Reference/Keyframes, Runway Gen-4.5 image-to-video, Midjourney Animate). Karakter ve kalabalık sahnelerinde bu yol en tutarlı sonucu verir.

```text
Efrasiyab, a mature Central Asian warrior king in his late forties, weathered sun-darkened face with high cheekbones and deep-set dark eyes, long straight dark hair worn loose past the shoulders, short dark beard, bareheaded, dark iron lamellar armor of small laced plates over a deep blue knee-length belted caftan, subtle dark fur mantle across the shoulders, leather belt with plain iron fittings, soft leather riding boots, standing over a rough leather map painted with simple rivers and mountains on a low wooden table inside a war council tent, seasoned commanders in dark lamellar armor and belted caftans around him, one commander pointing toward the distant horizon through the open tent flap, warriors tightening leather straps, inspecting conical iron helmets and stringing recurved bows, firelight from braziers on determined faces, tense silence, realistic historically inspired equipment, muted bronze and deep blue palette, cinematic photorealism, subtle film grain --ar 16:9 --raw --hd --no text, letters, labels, crown
```

Hareket promptu (görselden videoya):

```text
Slow, smooth lateral camera movement from left to right across the council; one commander points toward the horizon through the tent flap; warriors tighten straps, turn helmets in their hands and string bows; firelight flickers across their faces; everyone else holds still in tense silence.
```

## Bu sahneye özel kontroller

- Haritada yazı, etiket, pusula gülü ya da modern çizgiler var mı?
- Zırhlar sade lamel mi; dikenli, boynuzlu ya da fantastik zırh çıkmış mı?
- Efrasiyab diğer karakter sahneleriyle aynı mı?
- Kalabalık sahnede eller ve yüzler bozuluyor mu; komutan sayısı değişiyor mu?
- Yaylar çift kavisli (recurved) kısa yay mı; uzun İngiliz yayı mı?

## Notlar

- Çok kişili iç mekân; modeller kalabalıkta el ve yüz bozuyor. Komutan sayısını 3–4 ile sınırlamak sonucu iyileştirir ("three seasoned commanders").
- Harita deri üzerine boyanmış kaba çizimler olarak tarif edildi; "map" sözcüğü modern harita çağrıştırmasın diye negatif listede "printed map, grid lines" var.
