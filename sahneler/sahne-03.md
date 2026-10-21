# Sahne 3 — Mektup getiren hüdhüd

> Promptlar İngilizcedir; üreticiye İngilizce metni yapıştır. Ortak kurallar: [`stil-rehberi.md`](../stil-rehberi.md). Araç ayarları, negatif alan kuralları ve 480p test ön ayarı: [`sahne-01.md`](sahne-01.md).

## Orijinal prompt

```text
A realistic hoopoe bird with a distinctive orange crest and black-and-white wings flies across an ancient Central Asian royal garden toward an enormous steppe royal tent. The bird lands on a carved wooden post near the entrance, carrying a small folded parchment message tied with a simple cord. Gentle wind moves hanging fabrics, servants in historically inspired robes pause in surprise, slow tracking camera following the bird, natural daylight, cinematic realism, restrained historical atmosphere, 16:9, no magical glow, no readable writing, no subtitles.
```

## Çekim özeti

| Alan | Değer |
|---|---|
| Süre | 8 sn |
| Çekim | Takip çekimi, orta-geniş |
| Kamera | Kuşu uçuşundan konuşuna kadar izleyen yavaş takip |
| Lens | ~50–85 mm |
| Işık | Doğal gün ışığı |
| Mekân | Kraliyet bahçesi (kavaklar, meyve ağaçları, sulama arkları) ve büyük otağ girişi |
| Duygu | Sakin, şaşkınlık anı |

## Ana prompt

Veo 3.1 (Flow), Gemini Omni Flash 1.1 ve Kling 4.0 için olduğu gibi kullan. Negatif alanı olan araçlarda (Vertex Veo, Kling 3.0 Pro) son "Avoid: ..." cümlesini sil ve aşağıdaki negatif listeyi o alana koy. Runway Gen-4.5'te "Avoid" cümlesini sil; 1000 karakteri aşıyorsa anahtar kare + hareket promptu yolunu kullan.

```text
Cinematic realism, 16:9 widescreen, one continuous shot. A realistic Eurasian hoopoe with its distinctive orange crest tipped in black and bold black-and-white barred wings flies low across an ancient Central Asian royal garden of poplars, fruit trees and stone-lined water channels toward an enormous round royal tent of white felt. In its beak it carries a small folded parchment tied with a simple plain cord. The hoopoe lands on a carved wooden post beside the tent entrance and folds its wings. Gentle wind moves the hanging felt and woven fabrics at the entrance. Two servants in historically inspired belted robes pause in surprise and look up at the bird. Camera: slow, smooth tracking shot following the bird in flight to its landing. Natural daylight, restrained historical atmosphere, realistic feathers and wingbeats, muted bronze and deep blue palette, subtle film grain. The parchment is plain and blank on the outside. Avoid: magical glow, readable writing, subtitles.
```

Uzunluk: 983 karakter.

**Negatif prompt** (yalnızca negatif alanı olan araçlarda):

```text
magical glow, sparkles, light rays, glowing bird, readable writing, letters, runes, seal with text, cartoon bird, parrot, wrong bird species, extra wings, extra legs, distorted hands, text, subtitles, captions, letters, watermark, logo, modern objects, modern clothing, cartoon, CGI look, blurry, flicker
```

İsteğe bağlı ses satırı (ses üreten araçlarda promptun sonuna):

```text
Ambient noise: birdsong in a quiet garden, soft wind in poplar leaves, fabric rustling, the hoopoe's wingbeats and a short 'hoop-hoop' call. No music, no voices.
```

## Anahtar kare (Midjourney V8.2)

Önce bu kareyi üret, sonra görselden videoya canlandır (Kling 4.0 Omni Reference/Keyframes, Runway Gen-4.5 image-to-video, Midjourney Animate). Karakter ve kalabalık sahnelerinde bu yol en tutarlı sonucu verir.

```text
a realistic Eurasian hoopoe with an orange black-tipped crest and black-and-white barred wings perched on a carved wooden post beside the entrance of an enormous round white felt royal tent, a small folded blank parchment tied with a plain cord in its beak, ancient Central Asian royal garden with poplars and fruit trees behind, hanging woven fabrics moving in a gentle wind, two servants in belted robes looking up in surprise in the background, natural daylight, cinematic realism, restrained historical atmosphere, muted bronze and deep blue palette, photorealistic, subtle film grain --ar 16:9 --raw --hd --no text, letters, writing, glow
```

Hareket promptu (görselden videoya):

```text
The camera slowly tracks the hoopoe as it glides in and lands on the carved post, folding its wings and raising its crest; gentle wind moves the hanging fabrics; the two servants pause and look up in surprise; natural daylight, smooth steady camera.
```

## Bu sahneye özel kontroller

- Kuş gerçekten hüdhüd mü (turuncu, ucu siyah ibik; siyah-beyaz çizgili kanat)? Papağan ya da başka bir kuşa dönüşüyor mu?
- Parşömen boş mu; üzerinde okunabilir yazı, harf, mühür yazısı var mı?
- Kuşun etrafında parlama, ışık hüzmesi ya da sihirli toz var mı?
- Hizmetkârların elleri ve yüzleri doğal mı?
- Kuş inişte direkle kaynaşıyor ya da kanat sayısı değişiyor mu?

## Notlar

- Orijinalde mesajın nasıl taşındığı belirtilmemiş; kuş gerçekçi görünsün diye gagada tarif edildi. Ayağa bağlı istersen "tied to its leg" yaz; bu, posta güvercinine benzeyebilir.
- Kuş gibi küçük, hızlı hareket eden özneler modellerde sık bozuluyor. En sağlam yol: önce Midjourney ile kuşun direğe konduğu kareyi üret, sonra görselden videoya "kuşun konuşu" olarak canlandır (ya da son kare olarak kullan).
- Hüdhüd ve mektup motifi Hz. Süleyman kıssasını çağrıştırıyor; bu sahnede hiçbir peygamber ya da hükümdar gösterilmiyor, böyle kalması uygun.
