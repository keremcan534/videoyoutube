# videoyoutube

Antik Türk bozkırı temalı, yapay zekâ ile üretilen tarihî-epik bir YouTube videosu için sahne sahne prompt paketleri.

## Dosyalar

| Yol | İçerik |
|---|---|
| `sahne-listesi.md` | Tüm sahnelerin süre, çekim ve durum tablosu |
| `stil-rehberi.md` | Her sahneye eklenecek ortak stil bloğu, negatif liste, renk paleti, süreklilik notları, kalite kontrol listesi |
| `sahneler/sahne-NN.md` | Sahne başına: orijinal prompt, çekim özeti, ana prompt, 480p test ön ayarı, üreticiye göre promptlar (Veo 3.1, Gemini Omni, Runway, Kling, Midjourney) |
| `sahneler/_sablon.md` | Yeni sahne şablonu |
| `araclar/sahne01_test_render.py` | Sahne 1'in 480p/24 fps prosedürel test animatiğini üreten betik |
| `onizleme/` | Test videoları |

## Kullanım

1. `sahneler/sahne-NN.md` dosyasını aç, kullandığın üreticinin bölümündeki İngilizce promptu kopyala.
2. Araçta ayrı bir negatif alan varsa negatif listeyi oraya yapıştır; yoksa ana prompta ekleme.
3. Önce 480p test ön ayarıyla dene, sonra finali üret.
4. Klibi `stil-rehberi.md`'deki kalite kontrol listesine göre incele, `sahne-listesi.md`'de durumu güncelle.

## Yeni sahne

`sahneler/_sablon.md`'yi `sahne-NN.md` olarak kopyala, `stil-rehberi.md`'deki stil bloğunu promptun sonuna ekle ve `sahne-listesi.md`'ye bir satır ekle.

## Test animatiği

```bash
python3 araclar/sahne01_test_render.py            # onizleme/sahne-01-test-480p24.mp4 (854x480, 24 fps, 8 sn)
python3 araclar/sahne01_test_render.py --help     # çözünürlük, süre, fps, paralel iş sayısı
```

Gereken: Python 3, numpy, Pillow, ffmpeg. Bu bir yapay zekâ üretimi değil; kompozisyon, kamera hareketi, zamanlama ve palet testi içindir.
