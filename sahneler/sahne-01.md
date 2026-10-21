# Sahne 1 — Şafakta Bozkır (açılış planı)

> Promptlar İngilizcedir; üreticiye İngilizce metni yapıştır. Türkçe metinler yalnızca anlamak içindir.
> Bilgiler 21.10.2026 itibarıyla güncel kaynaklardan derlendi; model sürümleri hızlı değişir, üretimden önce aracın ayarlarını kontrol et.

## Orijinal prompt

```text
Cinematic historical epic establishing shot of the ancient Central Asian Turkic steppe at dawn, immense rugged mountains, endless grasslands, distant horsemen moving along the horizon, dark storm clouds gathering above the golden sunrise, wind sweeping across dry grass, slow aerial camera push forward, majestic scale, realistic natural lighting, muted bronze and deep blue palette, historically inspired ancient world, photorealistic, subtle film grain, 16:9 widescreen, no text, no subtitles, no modern objects, no fantasy magic effects.
```

## Çekim özeti

| Alan | Değer |
|---|---|
| Süre | 8 sn (araca göre 5–10 sn), tek kesintisiz çekim |
| Çekim tipi | Çok geniş, havadan açılış planı; kesme yok |
| Kamera | Alçak-orta irtifada yavaş, sabit ileri süzülüş; ufuk düz, sarsıntı ve yana yatma yok |
| Lens | Geniş, ~24–35 mm (full-frame karşılığı); ön plandaki otlardan dağlara kadar derin odak |
| Zaman | Şafak; güneş ufukta, alçak ve yatay altın ışık |
| Hava | Tepede toplanan koyu fırtına bulutları, altında parlayan gün doğumu, kuru otlarda güçlü rüzgâr, henüz yağmur yok; yaz sonu / sonbahar başı |
| Ana konu | Devasa sarp dağların önünde uçsuz bucaksız bozkır; ufukta minicik siluetler halinde ilerleyen küçük bir atlı kafilesi (5–20 atlı, tıknaz bozkır atları) |
| Duygu | Görkemli, ağırbaşlı, tekinsiz ama hayranlık uyandıran; destanın açılışında fırtına öncesi sessizlik |

## Ana prompt (her üretici için)

Orijinalin sözcükleri büyük ölçüde korundu. Yapılan değişiklikler ve nedenleri sayfanın sonundaki "Orijinale göre değişiklikler" bölümünde.

```text
Cinematic historical epic establishing shot, 16:9 widescreen: the ancient Central Asian Turkic steppe at dawn, a historically inspired world of early Turkic steppe nomads. Immense rugged mountains rise above endless grasslands. Far in the distance, a small file of horsemen on compact steppe horses moves slowly along the horizon, tiny dark silhouettes against the light. Dark storm clouds gather above, with a golden sunrise glowing beneath them on the horizon. Wind sweeps across the dry bronze grass in long rippling waves visible from above. Camera: slow, steady aerial push forward, smooth and level. Majestic scale, realistic natural lighting, muted bronze and deep blue palette, photorealistic, subtle film grain. Clean, untouched landscape. Avoid: text, subtitles, modern objects, fantasy magic effects.
```

**Negatif prompt** (yalnızca ayrı negatif alanı olan araçlar için; ana prompta yapıştırma):

```text
text, subtitles, captions, letters, watermark, logo, runes, morphing horses, extra legs, merged riders, floating riders, camera shake, camera roll, flicker, glowing magic effects, energy beams, roads, fences, power lines, buildings, vehicles, contrails, modern yurt camp, crop fields, plate armor, horned helmets, capes, turbans, emblem flags, Arabian horses, sand dunes, lush green grass, teal-orange grade, lens flare, blown-out sky, CGI look, cartoon, blurry
```

<details>
<summary>Ana promptun Türkçesi (anlamak için)</summary>

Sinematik tarihî destan tarzında, 16:9 geniş ekran, mekânı tanıtan genel plan: şafak vakti kadim Orta Asya Türk bozkırı; erken dönem Türk bozkır göçebelerinin tarihten ilham alan dünyası. Uçsuz bucaksız çayırların üzerinde devasa, sarp dağlar yükseliyor. Çok uzakta, tıknaz bozkır atlarına binmiş küçük bir atlı kafilesi ufuk çizgisi boyunca ağır ağır ilerliyor; ışığa karşı minicik koyu siluetler. Yukarıda koyu fırtına bulutları toplanıyor, altlarında ufukta altın rengi bir gün doğumu parlıyor. Rüzgâr kuru, bronz tonlu otları yukarıdan görülebilen uzun dalgalar halinde dalgalandırıyor. Kamera havadan yavaş ve sabit biçimde ileri süzülüyor; hareket akıcı, ufuk düz. Görkemli ölçek, gerçekçi doğal ışık, soluk bronz ve koyu mavi palet, fotogerçekçi, hafif film greni. Temiz, el değmemiş manzara. Kaçınılacaklar: yazı, altyazı, modern nesneler, fantastik büyü efektleri.

</details>

## Hızlı test ön ayarı: 480p / 24 fps

Final renderdan önce kompozisyonu, kamera hareketini ve atlıların ölçeğini ucuza denemek için. Hiçbir araç tam 854×480 vermiyor; 480p seçenekleri ~832–864 × 464–496 çıkıyor, gerekirse kurguda 854×480'e ölçekle/kırp.

| Araç | En düşük test çözünürlüğü | FPS | Not |
|---|---|---|---|
| **Seedance 2.0 Fast** (fal, Runware, BytePlus) | `resolution: "480p"`, `16:9` | 24 | Önerilen. Gerçekçilik ve hareket 480p'de en iyisi; ~0,07 $/sn (Runware). Seed girişi yok → ilk kare görseliyle sabitle |
| **Wan 3.0** (fal, Alibaba Model Studio) | `resolution: "480p"`, `aspect_ratio: "16:9"` (832×480) | Belgelenmemiş, ilk çıktıda kontrol et | En ucuz (~0,05 $/sn), seed verilebiliyor, 30 sn'ye kadar |
| **Midjourney Video** | SD ≈ 480p | 24 (üçüncü taraf) | Görselden videoya; HD'nin ~1/3 maliyeti |
| **Gemini Omni Flash 1.1** | 360p (640×360) | Belirtilmemiş | Google tarafında kalacaksan; 480p'nin altında, final görünümden farklı olabilir |
| **Luma Ray (Draft Mode)** | Draft (piksel boyutu açıklanmamış) | 24 | Çok ucuz, yalnızca uygulamada |
| Veo 3.1 / Runway Gen-4.5 / Kling 3.0–4.0 | 480p yok, en düşük **720p** | 24 (Runway'de 24/25 seçilebilir) | Test için en kısa süre + Fast/ucuz katman kullan |

**Testten finale geçerken:**

- Seed modeller arasında taşınmaz. Test geçişi kompozisyonu, kamera hareketini, atlıların boyunu ve temposunu doğrular; piksel önizlemesi değildir.
- Görünümü sabitlemek için bir 16:9 anahtar kare üret (aşağıdaki Midjourney bölümü) ve hem testte hem finalde onu **ilk kare** olarak kullan.
- Prompt metnini ve süreyi aynı tut.
- Finalle birebir benzerlik istiyorsan son kontrolü finaldeki modelin ucuz katmanında yap (ör. Veo 3.1 Fast, 720p), sonra 1080p'ye geç.
- Yerel deneme: `python3 araclar/sahne01_test_render.py` aynı kompozisyonu 854×480 / 24 fps prosedürel animatik olarak üretir (`onizleme/sahne-01-test-480p24.mp4`). Bu yapay zekâ üretimi değildir; zamanlama ve palet testi içindir.

## Üreticiye göre promptlar

> **Sora kullanılamıyor.** OpenAI, Sora uygulamasını 26.04.2026'da, Sora 2 API'sini 24.09.2026'da kapattı; resmî bir yerine geçen yok. Hâlâ "Sora 2" satan siteler büyük olasılıkla gerçek Sora değil.

### Google Veo 3.1 — Flow (labs.google/flow)

- **Model:** Veo 3.1 - Quality (test için Fast veya Lite)
- **Ayarlar:** 16:9 (Flow'un oran ayarından), 8 sn, 1080p (planın izin veriyorsa 4K), 2–4 çıktı
- **Ses:** Veo 3.1'de her zaman açık, kapatılamıyor; aşağıdaki ses satırıyla yönlendir ya da kurguda sustur.
- **Negatif alan:** Flow'da belgelenmiş bir negatif alan yok. Dışlamalar Google'ın önerdiği gibi sahnenin parçası olarak yazıldı ("no buildings or roads" kalıbı).

```text
Cinematic historical epic establishing shot. Slow, steady aerial drone shot gliding forward low over the grass toward immense rugged mountains, smooth constant speed, majestic scale. The ancient Central Asian Turkic steppe of the early Turkic nomads, at dawn: endless grasslands of dry feather grass stretch to the horizon. Far away, a small file of five horsemen on compact steppe horses moves slowly along the horizon, tiny silhouettes rim-lit by the low sun. Dark storm clouds slowly gather above a golden sunrise, with no lightning, and wind sweeps across the dry grass in long silvery waves. Realistic natural lighting, muted bronze and deep blue palette, historically inspired ancient world. Untouched wilderness with no buildings, roads, fences, power lines, vehicles or aircraft, and no signs or writing anywhere; a clean picture without on-screen lettering or captions, grounded and physically real light and weather. Photorealistic, subtle fine 35mm film grain, 16:9 widescreen.
```

İsteğe bağlı ses satırı (promptun en sonuna ekle):

```text
Ambient noise: strong steppe wind hissing through dry grass, a distant low rumble of thunder, faint muffled hoofbeats far away. Purely natural ambient sound only, wind and distant hooves, without music or voices.
```

Notlar: Tırnak işareti, diyalog, "documentary" veya "title" sözcükleri kullanılmadı; bunlar ekrana yazı/altyazı basılmasının başlıca nedenleri. Atlı sayısı 5'e indirildi çünkü Veo uzaktaki küçük figürlerde titreme ve şekil bozulması yapabiliyor. Hâlâ yazı ya da modern nesne çıkarsa gerçek negatif alanı olan Vertex yolunu kullan.

### Google Veo 3.1 — Vertex AI / Gemini Enterprise Agent Platform (API)

- **Model:** `veo-3.1-generate-001` (GA, us-central1). Test için `veo-3.1-fast-generate-001`.
- **Parametreler:** `aspectRatio: "16:9"`, `durationSeconds: 8`, `resolution: "1080p"`, `sampleCount: 2–4`, sabit bir `seed` (0–4294967295; sahneler arasında aynısını kullan), `negativePrompt` aşağıdaki gibi.
- **Dikkat:** Gemini API / AI Studio önizleme kimlikleri (`veo-3.1-generate-preview`, `veo-3.1-fast-generate-preview`, `veo-3.1-lite-generate-preview`) **22.10.2026'da kapanıyor**; bunları kullanan betikler/araçlar çalışmaz. GA modelin emeklilik tarihi "17.11.2026 veya sonrası"; her üretim partisinden önce yaşam döngüsü sayfasını kontrol et.

```text
Cinematic historical epic establishing shot. Slow, steady aerial drone shot gliding forward low over the grass toward immense rugged mountains, smooth constant speed, majestic scale. The ancient Central Asian Turkic steppe of the early Turkic nomads, at dawn: endless grasslands of dry feather grass stretch to the horizon. Far away, a small file of five horsemen on compact steppe horses moves slowly along the horizon, tiny silhouettes rim-lit by the low sun. Dark storm clouds gather above a golden sunrise, and wind sweeps across the dry grass in long silvery waves. Realistic natural lighting, muted bronze and deep blue palette, historically inspired ancient world, untouched wilderness. Photorealistic, subtle fine 35mm film grain, 16:9 widescreen.
```

`negativePrompt`:

```text
text, subtitles, captions, letters, runes, title card, watermark, logo, modern buildings, roads, tire tracks, fences, power lines, vehicles, aircraft, contrails, modern clothing, yurt camp, tents, crowd, close-up riders, glowing magic effects, energy beams, fantasy creatures, lightning, lens flare, scene cuts
```

Ses satırı: Flow'dakiyle aynı. Atlılar titrer ya da bozulursa sayıyı 3'e indir veya atlıları neredeyse durağan bırakıp hareketi kameraya ver.

### Gemini Omni Flash 1.1 — Gemini uygulaması, Flow, Gemini API

- **Model:** `gemini-omni-1.1-flash` (API) / Flow'da "Gemini Omni Flash 1.1". 19.05.2026'dan beri Gemini uygulamasının video aracı bu.
- **Ayarlar:** 16:9, 8 sn (en fazla 10 sn), 720p doğal (1080p/4K ölçeklenmiş). Hızlı test için 360p.
- **Negatif alan yok;** Google'ın kendi rehberi kısa satır içi olumsuzlamaları öneriyor. Başa "In a single continuous shot" yazılmazsa açılış planını birkaç kesmeye bölebiliyor.

```text
In a single continuous shot: a cinematic historical epic establishing shot of the ancient Central Asian Turkic steppe of the early Turkic nomads, at dawn. A slow, steady aerial drone shot glides forward low over endless grasslands of dry feather grass toward immense rugged mountains, majestic scale. Far away, a small file of five horsemen on compact steppe horses moves slowly along the horizon, tiny silhouettes rim-lit by the low sun. Dark storm clouds gather above a golden sunrise, and wind sweeps across the dry grass in long silvery waves. Realistic natural lighting, muted bronze and deep blue palette, historically inspired ancient world. Photorealistic, subtle fine 35mm film grain, 16:9 widescreen. No scene cuts. No close-ups of riders. No lightning. No text. No subtitles. No modern objects. No fantasy magic effects.
```

İsteğe bağlı ses satırı (ayrı satır olarak ekle):

```text
Sound design: howling steppe wind through dry grass, a distant low rumble of thunder, faint far-off hoofbeats. No dialogue. No music. No narration.
```

Yüksek çözünürlüklü final için Veo 3.1 daha iyi; Omni'yi hız ya da uygulama erişimi için kullan.

### Runway Gen-4.5

- **Model:** Tool mode → Video → model seçicide **Gen-4.5** (Runway Agent'ın seçmesine bırakma). API: `gen4.5`.
- **Ayarlar:** 16:9 (1280×720; API'de `ratio: "1280:720"`), 10 sn (2–10), Advanced settings'te 24 fps. Beğendiğin çekimde seed'i sabitle. Sonra Upscale (~4K) ve kurguda tam 3840×2160'a uydur. Standard plan ve üzeri, 12 kredi/sn.
- **Ses yok** (çıktıyı sessiz kabul et).
- **Negatif alan yok** ve Runway olumsuz ifadeleri açıkça önermiyor ("ters sonuç verebilir"). Bu yüzden dışlamalar olumlu yazıldı: "Clean frame", "untouched wild land", "realistic weather and light". 1000 karakter sınırı var; bu prompt 989 karakter. Bir şey eklemeden önce bir şey çıkar (ilk aday: "subtle film grain"; greni kurguda ekleyebilirsin).

```text
Cinematic historical epic: aerial extreme wide establishing shot of the ancient Central Asian Turkic steppe at dawn, a historically inspired ancient world of early Turkic nomads. The camera pushes forward slowly and steadily, gliding at a high, constant altitude above endless grasslands of dry golden feather grass toward immense rugged mountains that grow larger as it advances. Far ahead, a single-file line of about ten distant horsemen on compact steppe horses moves at a walk along the horizon from left to right, tiny silhouettes that reveal the majestic scale of the land. Dark storm clouds gather above, and a low band of golden sunrise light breaks beneath them. Wind sweeps across the dry grass in long rippling waves. Realistic natural lighting, muted bronze and deep blue palette, photorealistic, subtle film grain. Clean frame of untouched wild land, riders in belted knee-length robes with bow cases at the hip, realistic weather and light. Continuous, seamless single shot.
```

Görselden videoya (Gen-4.5 image-to-video, 16:9, 10 sn) hareket promptu:

```text
The camera pushes forward slowly and steadily in a high aerial glide above the grass as the mountains grow larger. The distant horsemen ride at a steady walk from left to right along the horizon. Wind sweeps across the dry grass in long rippling waves, and the dark storm clouds drift and gather above the golden sunrise. Continuous, seamless single shot.
```

Ses için ayrı bir SFX aracına (Runway SFX, ElevenLabs vb.) şunu ver; video promptuna ekleme: `Steppe wind gusting through dry grass, faint distant hoofbeats at a walk, far-off rolling thunder; no music, no voices, no narration.`

Sorun çıkarsa:

- **Atlılar bozuluyor:** görselden videoya yolunu kullan.
- **İtme hızlı:** "very slow, smooth, steady" ekle.
- **Yeşil/kuru ot karışıyor:** "late summer" ekle.
- **Otlardaki rüzgâr görünmüyor:** "high, constant altitude" yerine "moderate, constant height" yaz.

### Kling 4.0 (yedek: Kling VIDEO 3.0 Pro)

- **Model:** Kling 4.0, tam sürüm; Flash değil, çünkü Flash ilk kare desteklemiyor. 15.10.2026'da çıktı; kling.ai web ve uygulamada. API ile çalışıyorsan ya da ayrı negatif alan istiyorsan 3.0 Pro.
- **Ayarlar:** 16:9 elle seç (Omni Reference varsayılanı "Auto"). 10 sn (tek itme için 8–10 sn güvenli; 20–30 sn kayma yapar). 1080p (4K katmana bağlı). Tek çekim, multi-shot kapalı. Seed görünüyorsa sabitle. 2–4 çekim al, atların bacaklarını kare kare kontrol et.
- **Ses:** 4.0'da aç/kapa belgelenmemiş, prompt ile yönlendir. 3.0'da kendi sesini ekleyeceksen `sound` / `generate_audio` kapat. Kling Türkçe konuşma üretemiyor; Türkçe anlatımı ayrıca kaydet.

```text
Cinematic historical epic establishing shot, an extreme long shot from the air: the ancient Central Asian Turkic steppe at dawn, ancient Inner Asia. Endless grasslands of dry golden grass stretch toward immense rugged mountains. Along the far horizon, about ten distant horsemen on compact steppe horses walk slowly in single file from left to right, each rider and horse separate and solid, tiny dark silhouettes rim-lit by the sun. Dark storm clouds gather above the golden sunrise. Wind sweeps across the dry grass in long rippling waves while the clouds drift slowly in real time. Camera: one slow aerial push forward in a single continuous take, the camera gliding low and steadily over the grassland toward the mountains at a constant speed, smooth and stable, with no speed changes and no cuts. Majestic scale: the riders are tiny against the vast plain and the immense mountains. Realistic natural lighting, natural weather and natural light only. Muted bronze and deep blue palette: bronze-gold grass and sunrise against deep blue mountain shadows and storm sky. Historically inspired ancient world, untouched wilderness with only grass, rock, sky, riders and horses. Photorealistic, subtle film grain, 16:9 widescreen. No subtitles, no on-screen text, no background music.
```

**Yalnızca Kling 3.0 Pro:** Advanced Settings → Negative Prompt alanına (API: `negative_prompt`) yapıştır. Kling 4.0'da belgelenmiş negatif alan yok; orada kullanma.

```text
text, subtitles, captions, letters, watermark, logo, buildings, roads, fences, power lines, vehicles, aircraft, contrails, drone, magic glow, sparks, energy beams, glowing runes, time-lapse clouds, flicker, morphing, merged horses, extra legs, blur, low quality
```

İsteğe bağlı ses satırı ("16:9 widescreen." ile kapanış cümlesi arasına):

```text
Audio: strong steppe wind hissing through dry grass, distant rolling thunder, faint far-off hoofbeats; ambient sound effects only, no music, no dialogue, no voice-over, no narration.
```

**Görselden videoya** (Midjourney anahtar karesiyle; iki yoldan birini seç, ikisi aynı görevde birleştirilemez):

- **(a) Omni Reference:** görseli referans olarak yükle, oranı elle 16:9 yap ve şunu kullan:

  ```text
  @Image1 is the first frame. Slow aerial push forward in one continuous take: the camera glides low and steadily over the grassland toward the immense rugged mountains at a constant speed, smooth and stable, no speed changes, no cuts. Wind sweeps across the dry grass in long rippling waves. The distant horsemen walk slowly in single file from left to right along the horizon, each rider and horse separate and solid. Dark storm clouds gather slowly above the golden sunrise in real time. Realistic natural lighting, natural weather and natural light only; keep the muted bronze and deep blue palette of the frame. No subtitles, no on-screen text, no background music.
  ```

- **(b) Keyframes (yalnızca ilk kare):** görseli ilk kare yuvasına yükle (oran ondan alınır). Aynı promptu baştaki `@Image1 is the first frame.` cümlesi olmadan kullan.

Çekim başına 10 sn'de 2–3 bozuk kare beklenebilir. Gren kaynarsa "subtle film grain"i çıkar, greni kurguda ekle.

### Midjourney V8.2 — 16:9 anahtar kare + Midjourney Video (Animate)

- **Model:** V8.2'yi web Settings'ten seç (bayrakla değil). İş bilgilerinde V8.2 yazdığını kontrol et.
- **Ayarlar:** `--ar 16:9 --raw --hd`; `--stylize` varsayılan 100 (daha birebir için 50). Kişiselleştirme, moodboard ve sref kapalı olsun ya da tek bir `--sref` sabitle ki sonraki sahneler eşleşsin.
- **Animate:** Manual, önce `--motion low` (kamera kıpırdamazsa `--motion high`); maliyet için `--bs 1` veya `2`. HD video 720p; test için SD ≈ 480p. Klip ~5 sn, bir kez uzatınca ~9 sn. Ses yok.
- YouTube masterı için aynı kareyi Kling 4.0'da 1080p/4K canlandırmak daha iyi; Midjourney Video en fazla 720p.

Anahtar kare promptu:

```text
Cinematic historical epic establishing shot, aerial view of the ancient Central Asian Turkic steppe at dawn, ancient Inner Asia, endless grasslands of dry golden grass, wind sweeping across the dry grass and bending it in long waves, immense rugged mountains, distant horsemen on compact steppe horses moving along the horizon as a small file of tiny rim-lit silhouettes on the far horizon line, dark storm clouds gathering above the golden sunrise, open empty grassland in the foreground leading toward the mountains, majestic scale, realistic natural lighting, natural light only, muted bronze and deep blue palette, historically inspired ancient world, untouched wilderness, photorealistic, subtle film grain --ar 16:9 --raw --hd --no text, letters, buildings, roads, vehicles, pylons, sparkles
```

Neden böyle:

- `--no` her sözcüğü ayrı okur. "power lines" yazılsaydı "lines" da yasaklanır, ufuk çizgisi ve atlı dizisi zarar görürdü; bu yüzden "pylons" kullanıldı.
- Gün doğumu ışıltısı bastırılmasın diye "glow" listeye eklenmedi.

Canlandırmadan önce atlılara yakınlaş; kaynaşmış at-binici lekelerini Vary Region ya da V8.2 Edit ile düzelt, sonra HD'yi yeniden çalıştır.

Hareket promptu (Midjourney Animate; Runway/Kling görselden videoya için de uygun):

```text
Slow, steady aerial push forward toward the immense rugged mountains, the camera gliding low over the grassland at a constant speed in one continuous take; wind sweeps across the dry grass in long rippling waves; the distant horsemen walk slowly in single file from left to right along the horizon, each rider and horse separate and solid; dark storm clouds drift and gather slowly above the golden sunrise; realistic natural light, smooth stable camera.
```

## Tarihî çerçeve (kısa)

- **Dönem:** Hikâye Efrasiyab (Alp Er Tunga) etrafında döndüğü için efsanevi bir çağda geçiyor; bu yüzden promptlarda belirli bir yüzyıl yazılmadı ("historically inspired"). Görsel ayrıntılar (at, eyer, kaftan, yay) belgelenmiş en erken Türk dönemi olan Göktürk Kağanlığı'ndan (552–744) besleniyor; bu, dönemi tahmin etmek için güvenli bir referans.
- **Coğrafya:** Karlı sivri zirveler + geniş bozkır en iyi **Altay**'a (Zhoushu'daki "Altın Dağ") ya da **Tanrı Dağları**'na uyar. Sahne Ötüken/Orhun Vadisi diye tanıtılacaksa dağları yuvarlak sırtlı, ormanlı yamaçlı ve karsız göster.
- **Otlar:** Moğol bozkırına sorguç otu (*Stipa*) hâkim; gümüşi kılçıkları rüzgârda belirgin dalgalanır. Kuru altın ot yaz sonu / sonbahar başını gösterir.
- **Atlılar (uzaktan):**
  - **At ve eyer:** Kısa bacaklı, kalın boyunlu, gür yeleli bozkır atları; ahşap iskeletli sert eyer ve üzengi.
  - **Silahlar:** Kalçada yay kılıfı ve sadak, birkaç dik mızrak.
  - **Giyim:** Diz boyu kuşaklı kaftan; sade başlık ya da yuvarlak-konik miğfer.
  - **Sancak:** En fazla bir tane, uçta küçük koyu bir tepelik veya tuğ. Amblemli dikdörtgen bayrak kullanma.
- **Kaçınılacaklar:**
  - **Başka çağ ve kültürlerin klişeleri:** 13. yüzyıl Moğol İmparatorluğu klişeleri, Avrupa şövalyeleri, Arap çölü motifleri, boynuzlu miğfer, pelerin, sarık, modern mavi "Göktürk bayrağı".
  - **Modern izler:** Yol, çit, elektrik hattı, uçak izi.

## Kalite kontrol

`stil-rehberi.md`'deki ortak kontrol listesine ek olarak bu sahnede özellikle:

- Atlılar klip boyunca ufukta küçük ve uzak kalıyor mu; sayıları değişiyor, birbirine kaynaşıyor ya da havada süzülüyor mu?
- Güneş fırtına bulutlarının **altında**, ufukta mı; gökyüzü beyaza patlamış mı?
- Kamera tek, yavaş, düzgün bir ileri süzülüş mü; otların içine dalıyor ya da ufuk yana yatıyor mu?
- Ot tek mevsimi mi gösteriyor (kuru, altın-bronz); rüzgâr dalgaları doğal ve sürekli mi?

## Orijinale göre değişiklikler (ana prompt)

- **"16:9 widescreen" başa alındı.** Biçim ve kadraj içerikten önce gelsin diye; oranı yine de aracın ayarlarından seç.
- **"historically inspired ancient world" ayar cümlesine katıldı.** "early Turkic steppe nomads" olarak yazıldı. Tek başına "ancient" Greko-Romen çağrışımı yapabiliyor; 6.–8. yüzyıl tarihinin yanında ikinci kez "ancient" çelişkili duruyordu.
- **Atlılar netleştirildi:** "a small file of horsemen on compact steppe horses ... tiny dark silhouettes". Arap/yük atı biçimlerini engeller. Az ve küçük atlı, modellerin bacak bozma riskini düşürür.
- **Güneş bulutların altına yerleştirildi:** "golden sunrise glowing beneath them on the horizon". Şafak ışığı görünür kalır.
- **Rüzgâr görünür kılındı:** "long rippling waves visible from above". Havadan çekimin gösterebileceği somut bir hareket.
- **Kamera ayrı etiketle yazıldı:** "Camera: slow, steady aerial push forward, smooth and level". Sarsıntıyı, yana yatmayı ve hız değişimini azaltır.
- **Dört "no ..." ifadesi tek kapanış cümlesinde toplandı:** "Avoid: ...". Önüne olumlu bir ifade ("Clean, untouched landscape") eklendi. Somut örnekler (yollar, elektrik hatları, run harfleri...) yalnızca negatif listede.
