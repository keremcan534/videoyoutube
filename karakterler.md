# Karakterler

Aynı karakterin her sahnede aynı görünmesi için sabit tanım blokları. Karakterin geçtiği her sahnede bloğu **kelimesi kelimesine** aynı yaz; yalnızca poz, ifade ve eylemi değiştir.

## Efrasiyab (Alp Er Tunga)

Sahneler: 2, 4, 5 (7 ve 8'de yalnızca ordusu var, kendisi görünmüyor).

Tanım bloğu:

```text
Efrasiyab, a mature Central Asian warrior king in his late forties, weathered sun-darkened face with high cheekbones and deep-set dark eyes, long straight dark hair worn loose past the shoulders, short dark beard, bareheaded, dark iron lamellar armor of small laced plates over a deep blue knee-length belted caftan, subtle dark fur mantle across the shoulders, leather belt with plain iron fittings, soft leather riding boots
```

Neden böyle:

- **Taç yok, başı açık.** Orijinaldeki "no crown fantasy" isteği olumlu yazıldı: "bareheaded". Modeller "king" sözcüğünü görünce sıklıkla altın taç ekliyor. Taç yine çıkarsa negatif listeye `crown, tiara, golden helmet` ekle.
- **Yaş ve yüz.** "Late forties", "high cheekbones" ve "deep-set dark eyes" sahneler arasında yüzün kaymasını azaltır.
- **Kıyafet.** Kaftan rengi (deep blue) paletle uyumlu ve her sahnede aynı.
- **Göz.** Gözler parlamasın diye negatif listeye `glowing eyes` ekle; promptta "natural eyes" yeter.

### Atı

```text
a powerful black steppe warhorse, compact and muscular, thick neck, heavy mane and full tail, plain dark leather bridle, wooden-framed saddle with iron stirrups
```

Uzun bacaklı Arap atı ya da Friz atı biçimi istemiyoruz; stil rehberindeki bozkır atı tipiyle aynı.

## Karakter tutarlılığı: referans görsel yöntemi

Metin tek başına yüzü sahneden sahneye sabit tutmaz. En güvenilir yol:

1. **Referans görselleri üret.** Midjourney V8.2 (veya başka bir görsel modeli) ile Efrasiyab için bir referans seti yap. Nötr gri fon, aynı ışık; önden yakın plan, 3/4 açı ve boy çekimi. Tanım bloğunu kullan, sonuna `--ar 2:3 --raw` ekle.
2. **En iyi yüzü seç** ve bu görselleri `referanslar/efrasiyab/` klasörüne koy.
3. **Her karakter sahnesinde aynı görseli referans ver:**
   - **Kling 4.0:** Omni Reference'ta karakter görselini `@Image1` olarak ekle.
   - **Runway Gen-4.5:** Önce bir anahtar kare yap (karakter referansıyla), sonra görselden videoya.
   - **Veo 3.1:** Flow'da referans görselli üretim seçeneği varsa onu kullan. Yoksa önce anahtar kareyi üretip görselden videoya git.
   - **Midjourney V8.2:** Edit modeli en fazla 4 referans görsel alıyor.
4. **Sahnenin ilk karesini üret** (karakter + mekân), sonra görselden videoya canlandır. Bu, sahneler arasında yüzü en iyi koruyan yol.

> Not: Araçların referans özellikleri sık değişiyor. Yukarıdaki adlar 21.10.2026'daki araştırmaya dayanıyor; Veo'nun referans görsel desteği arayüzde doğrulanmadı.
