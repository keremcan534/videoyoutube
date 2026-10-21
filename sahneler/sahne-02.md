# Sahne 2 — Efrasiyab ve kara atı

> Promptlar İngilizcedir; üreticiye İngilizce metni yapıştır. Ortak kurallar: [`stil-rehberi.md`](../stil-rehberi.md). Araç ayarları, negatif alan kuralları ve 480p test ön ayarı: [`sahne-01.md`](sahne-01.md). Karakter tanımı: [`karakterler.md`](../karakterler.md).

## Orijinal prompt

```text
A formidable ancient Turkic epic king, Efrasiyab, a mature Central Asian warrior with a weathered face, long dark hair, a short dark beard, dark iron lamellar armor, subtle fur mantle, standing beside a powerful black warhorse outside a vast traditional steppe royal tent. His expression is proud, intelligent and unafraid. Wind moves his cloak and horse's mane. Slow low-angle camera orbit, realistic human proportions, grounded historical costume, dramatic overcast light, restrained colors, photorealistic cinematic historical epic, 16:9, no crown fantasy, no glowing eyes, no text.
```

## Çekim özeti

| Alan | Değer |
|---|---|
| Süre | 8 sn |
| Çekim | Alçak açı, orta-geniş; karakter tanıtımı |
| Kamera | Yavaş alçak açılı yörünge (yarım tur), sabit hız |
| Lens | ~35–50 mm, hafif sığ alan |
| Işık | Dramatik kapalı hava ışığı, yumuşak gölgeler |
| Mekân | Açık bozkırda büyük, beyaz keçe kraliyet otağı |
| Duygu | Gururlu, zeki, korkusuz |

## Ana prompt

Veo 3.1 (Flow), Gemini Omni Flash 1.1 ve Kling 4.0 için olduğu gibi kullan. Negatif alanı olan araçlarda (Vertex Veo, Kling 3.0 Pro) son "Avoid: ..." cümlesini sil ve aşağıdaki negatif listeyi o alana koy. Runway Gen-4.5'te "Avoid" cümlesini sil; 1000 karakteri aşıyorsa anahtar kare + hareket promptu yolunu kullan.

```text
Photorealistic cinematic historical epic, low-angle medium-wide shot, 16:9 widescreen. Efrasiyab, a mature Central Asian warrior king in his late forties, weathered sun-darkened face with high cheekbones and deep-set dark eyes, long straight dark hair worn loose past the shoulders, short dark beard, bareheaded, dark iron lamellar armor of small laced plates over a deep blue knee-length belted caftan, subtle dark fur mantle across the shoulders, leather belt with plain iron fittings, soft leather riding boots, stands proudly beside a powerful black steppe warhorse, compact and muscular, thick neck, heavy mane and full tail, plain dark leather bridle, wooden-framed saddle with iron stirrups, outside a vast round royal tent of white felt with a domed roof, standing alone on the open steppe. His expression is proud, intelligent and unafraid; natural eyes, a calm, steady gaze. Wind moves his fur mantle, his long hair and the horse's mane. Camera: slow, smooth low-angle orbit around him, a half circle at constant speed. Realistic human proportions, grounded historical costume, dramatic overcast light, restrained colors, muted bronze and deep blue palette, subtle film grain. Avoid: crown, fantasy headgear, glowing eyes, text.
```

Uzunluk: 1238 karakter.

**Negatif prompt** (yalnızca negatif alanı olan araçlarda):

```text
crown, tiara, golden helmet, horned helmet, fantasy headgear, glowing eyes, magic glow, plate armor, European knight, cape clasp, extra fingers, distorted hands, extra legs, morphing horse, Arabian horse, text, subtitles, captions, letters, watermark, logo, modern objects, modern clothing, cartoon, CGI look, blurry, flicker
```

İsteğe bağlı ses satırı (ses üreten araçlarda promptun sonuna):

```text
Ambient noise: steady steppe wind, felt tent fabric flapping, the horse snorting softly and shifting its hooves. No music, no voices.
```

## Anahtar kare (Midjourney V8.2)

Önce bu kareyi üret, sonra görselden videoya canlandır (Kling 4.0 Omni Reference/Keyframes, Runway Gen-4.5 image-to-video, Midjourney Animate). Karakter ve kalabalık sahnelerinde bu yol en tutarlı sonucu verir.

```text
Efrasiyab, a mature Central Asian warrior king in his late forties, weathered sun-darkened face with high cheekbones and deep-set dark eyes, long straight dark hair worn loose past the shoulders, short dark beard, bareheaded, dark iron lamellar armor of small laced plates over a deep blue knee-length belted caftan, subtle dark fur mantle across the shoulders, leather belt with plain iron fittings, soft leather riding boots, standing beside a powerful black steppe warhorse, compact and muscular, thick neck, heavy mane and full tail, plain dark leather bridle, wooden-framed saddle with iron stirrups, outside a vast round white felt royal tent on the open steppe, proud intelligent unafraid expression, wind in his fur mantle and the horse's mane, low-angle view, dramatic overcast light, restrained colors, muted bronze and deep blue palette, photorealistic cinematic historical epic, subtle film grain --ar 16:9 --raw --hd --no crown, tiara, text, letters, glow
```

Hareket promptu (görselden videoya):

```text
Slow, smooth low-angle orbit around the king, a half circle at constant speed; wind moves his fur mantle, his long hair and the horse's mane; the horse shifts its weight and breathes; the king stays still and composed with a steady gaze; natural overcast light.
```

## Bu sahneye özel kontroller

- Başında taç, altın miğfer ya da fantastik başlık var mı?
- Gözler doğal mı; parlama, renkli ışık var mı?
- Yüz ve eller bozuk mu (fazla parmak, kayan yüz hatları)?
- Yörünge sırasında yüz başka birine dönüşüyor ya da zırh/kaftan rengi değişiyor mu?
- At tıknaz bozkır atı mı; bacak sayısı ve eklemleri doğru mu?

## Notlar

- Karakter tutarlılığı için önce `karakterler.md`'deki yöntemle referans görsel üret; bu sahneyi görselden videoya canlandırmak yüzü 4. ve 5. sahnelerle eşleştirir.
- Orijinaldeki "cloak" (pelerin), tanım bloğundaki kürk mantoyla eşleşsin diye "fur mantle" oldu; ayrı bir pelerin istersen ekle, ama "cape" Avrupa şövalyesi çağrıştırabilir.
- Otağ: bozkır kraliyet çadırı (otağ) beyaz keçeden, kubbeli ve büyük olarak tarif edildi; Göktürk kaynaklarında hükümdarın büyük keçe çadırı geçer.
