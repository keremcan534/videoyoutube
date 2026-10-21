# Stil rehberi

Tüm sahnelerin aynı videonun parçası gibi görünmesi için ortak kurallar. Sahne 1'den türetildi.

## Stil bloğu

Her sahnenin İngilizce promptunun **sonuna** ekle. Bilerek sahneye özel içerik (şafak, fırtına, atlılar) ve dönem içermiyor; dönemi her sahnenin kendi promptuna yaz.

```text
Photorealistic cinematic historical epic, historically inspired world of the Inner Asian steppe nomads, realistic natural lighting, restrained contrast, soft highlight roll-off, muted bronze and deep blue palette, subtle fine film grain, 16:9 widescreen, clean frame.
```

> Türkçesi: Fotogerçekçi, sinematik tarihî destan; İç Asya bozkır göçebelerinin tarihten ilham alan dünyası, gerçekçi doğal ışık, ölçülü kontrast, parlak alanlarda yumuşak geçiş, soluk bronz ve koyu mavi palet, hafif ince film greni, 16:9 geniş ekran, temiz kadraj.

## Ortak negatif liste

Negatif alanı olan araçlarda (Vertex Veo, Kling 3.0 Pro vb.) kullan; sahneye göre ekleme yap. Liste önem sırasına göre dizili; sınır darsa sondan kısalt.

```text
text, subtitles, captions, letters, watermark, logo, runes, morphing horses, extra legs, merged riders, floating riders, camera shake, camera roll, flicker, glowing magic effects, energy beams, roads, fences, power lines, buildings, vehicles, contrails, modern yurt camp, crop fields, plate armor, horned helmets, capes, turbans, emblem flags, Arabian horses, sand dunes, lush green grass, teal-orange grade, lens flare, blown-out sky, CGI look, cartoon, blurry
```

Negatif alanı olmayan araçlarda (Runway Gen-4.5, Midjourney Video) "no X" yazma; istediğini olumlu tarif et ("clean frame", "untouched wilderness", "natural light only"). Midjourney görselinde `--no` parametresini tek sözcüklerle kullan.

## Renk paleti

| Renk | Hex | Kullanım |
|---|---|---|
| Fırtına Çividi | `#1C2433` | Fırtına bulutlarının altı, gökyüzünün üst bandı; karedeki en koyu mavi |
| Bozkır Mavisi | `#2C3E57` | Gün doğumu öncesi gölgedeki dağlar ve vadiler; uzak sırtlar |
| Buzul Kurşunisi | `#5B6E85` | Pus katmanları, gölgedeki kar ve kaya, gökyüzünün gün doğumu bandına geçişi |
| Soluk Güneş Pirinci | `#E0BE7E` | Güneş ışıltısı, aydınlanan zirveler, atlılardaki kenar ışığı; en açık değer, saf beyaza patlatma |
| Antik Altın | `#B88A44` | Ufuktaki gün doğumu bandı, ot uçlarındaki parlaklık |
| Yanık Bronz | `#8A5E34` | Güneş alan kuru otun orta tonları, at postu, arkadan aydınlanan toz |
| Kuru Bozkır Okrası | `#9C8462` | Yarı ışıktaki çayırın gövdesi; bronz parlaklıktan gölgeye geçiş |
| Yıpranmış Toprak | `#3A2C22` | Atlı ve at siluetleri, ön plandaki zemin gölgesi; soğuk maviler karşısında sıcak siyah |

## Süreklilik notları

- Üreticiye her zaman İngilizce promptu yapıştır. Türkçe metin yalnızca anlamak içindir; Türkçe sözcükler görüntüye yazı olarak da sızabilir.
- **Dönem etiketleri:** Göktürk dönemi (6.–8. yüzyıl) sahnelerinde dönemi promptta belirt. Daha önceki çağlara (Hunlar/Xiongnu, Sakalar) geçen sahneleri "Türk" değil "bozkır halkları" diye etiketle.
- **Atlar:** Her sahnede aynı tip olsun: kısa bacaklı, kalın boyunlu, gür yeleli ve kuyruklu bozkır atları. Ahşap iskeletli sert eyer ve üzengi kullan. Arap atı ya da Batı tipi eyer kullanma.
- **Biniciler:** Diz boyu kuşaklı kaftan, pantolon, yumuşak çizme, sade başlık veya yuvarlak-konik miğfer; kalçada yay kılıfı ve sadak, birkaç dik mızrak. Boynuz, pelerin, sarık veya Avrupa zırhı olmasın.
- **Coğrafya:** Karlı sivri zirveler Altay veya Tanrı Dağları'na uyar. Ötüken/Orhun Vadisi sahnelerinde dağlar yuvarlak sırtlı, ormanlı yamaçlı ve karsız olsun.
- **Mevsim:** Kuru, altın-bronz tonlu çimen (yaz sonu / sonbahar başı). Hikâye zamanın geçtiğini anlatmıyorsa yemyeşil çayıra geçme.
- **Gökyüzü:** Fırtına havası bir hikâye ipucu. Sonraki dış mekân sahneleri ya bu gergin havayı sürdürsün ya da fırtınanın gelişini veya dağılışını bilinçli olarak göstersin; rastgele açık mavi gökyüzüne geçme.
- **Kamera dili:** Yavaş, sabit, ağırbaşlı hareketler. Hızlı drone dalışı ya da el kamerası sarsıntısını yalnızca aksiyon sahnelerinde ve bilerek kullan.
- **Yazı ve sembol:** Hiçbir sahnede yazı, altyazı, run harfi ve logo olmasın; altyazı ve başlıkları kurguda ekle. Orhun yazıtları, balballar ve kurt başlı sancak yalnızca hikâye gerektirdiğinde, ayrı sahnelerde ve tarihî doğruluğu kontrol edilerek gösterilsin. Modern mavi "Göktürk bayrağı" kullanılmasın.
- **Biçim:** Tüm klipler 16:9. En-boy oranını aracın ayarlarından seç, yalnızca prompta güvenme.
- **Seed ve tutarlılık:** Seed destekleyen araçlarda (Vertex Veo, Wan, Runway) aynı seed'i sahneler boyunca kullan. Seed modeller arasında taşınmaz; görünümü sabitlemek için ilk kare görseli kullan.

## Ortak kalite kontrol listesi

Her üretilen klibi kullanmadan önce:

1. Görüntünün herhangi bir yerinde yazı, altyazı, harf, run harfi/yazıt benzeri işaret, logo veya filigran var mı? Varsa klibi kullanma ya da o bölümü kırp.
2. Modern bir iz var mı: yol, tekerlek izi, çit, elektrik direği/hattı, bina, araç, uçak izi, güneş paneli, modern çadır kampı, sürülmüş tarla, saman balyası?
3. Atlılar ve atlar bozuluyor mu: fazla/eksik bacak, birbirine kaynaşan atlılar, havada süzülen figürler, geri geri yürüyen atlar?
4. Atlar kısa boylu, tıknaz bozkır atı gibi mi; uzun bacaklı Arap atı, iri yük atı ya da bembeyaz "kahraman atı" çıkmış mı?
5. Siluetlerde döneme aykırı bir şey var mı: boynuzlu miğfer, pelerin, şövalye zırhı, sarık, amblemli dikdörtgen bayrak, ateşli silah?
6. Fantastik/büyülü efekt var mı: parlayan ışınlar, renkli şimşek, enerji halesi, ejderha, dev kurt, doğal olmayan ışık hüzmeleri?
7. Kamera hareketi tek, yavaş ve düzgün mü; sarsıntı, titreme, ufkun yana yatması, ani hız değişimi veya kesme var mı?
8. Işık mantıklı mı: gölgeler aynı yöne mi düşüyor, gökyüzü veya güneş beyaza patlamış mı?
9. Renkler soluk bronz ve koyu mavi çizgisinde mi; aşırı doygun turuncu-camgöbeği (teal-orange) düzeltme ya da soğuk/gümüşi çimen tonu var mı?
10. Ufuk, dağlar veya bulutlar klip boyunca eriyip şekil değiştiriyor ya da titriyor mu? Görüntü 16:9 ve keskin mi; gren hafif mi, yoksa ağır eski film görünümüne mi kaçmış?
