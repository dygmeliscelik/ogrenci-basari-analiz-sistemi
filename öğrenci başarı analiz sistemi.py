import numpy as np

ogrenciler = np.array([
    "ada","bora","ceren","deniz","ece","firat"
])

notlar = np.array([
   [70,85,90,80],
   [45,60,55,50],
   [90,95,85,100],
   [65,70,60,75],
   [80,78,92,85],
   [30,45,55,40]
])

agirliklar = np.array([0.15,0.20,0.25,0.40])

agirlikli_notlar = np.sum(notlar * agirliklar, axis=1)
print(agirlikli_notlar)

basarili_mi = agirlikli_notlar >= 60
print(basarili_mi)

basarili_ogrenciler = ogrenciler[basarili_mi]
print(basarili_ogrenciler)

basarisiz_ogrenciler = ogrenciler[~basarili_mi]

print(basarisiz_ogrenciler)

basarili_sayisi = np.sum(basarili_mi)
basarisiz_sayisi = np.sum(~basarili_mi)

print("başarılı:", basarili_sayisi)
print("başarısız:", basarisiz_sayisi)

sinav_ortalamalari = np.mean(notlar, axis=0)
en_zor = np.argmin(sinav_ortalamalari)
en_kolay = np.argmax(sinav_ortalamalari)

print("en zor sınav:",en_zor + 1)
print("en kolay sınav:", en_kolay + 1)
print("sınav ortalamaları:", sinav_ortalamalari)

en_yuksek_not = np.max(agirlikli_notlar)
en_düşük_not = np.min(agirlikli_notlar)

en_yuksek_index = np.argmax(agirlikli_notlar)
en_düşük_index = np.argmin(agirlikli_notlar)

print("en başarılı öğrenci:", ogrenciler[en_yuksek_index])
print("en yüksek not:", en_yuksek_not)

print("en düşük not alan:", ogrenciler[en_düşük_index])
print("en düşük not:", en_düşük_not)

sinif_ortalamasi = np.mean(agirlikli_notlar)

print("sınıf ortalaması:", sinif_ortalamasi)

yeni_notlar = notlar.copy()
kosul = yeni_notlar[:, 3] < 70

yeni_notlar[kosul,3] = np.minimum(yeni_notlar[kosul, 3] + 10,100)

print("yeni notlar:")
print(yeni_notlar)

yeni_ortalama = np.sum(yeni_notlar * agirliklar, axis=1)

print("yeni ağırlıklı ortalamalar:", yeni_ortalama)

eski_durum = agirlikli_notlar >= 60
yeni_durum = yeni_ortalama >= 60

degisenler = eski_durum != yeni_durum

degisen_sayisi = np.sum(degisenler)

print("durumu değişen öğrenci sayısı:",degisen_sayisi)

class SinifAnalizi:

    def __init__(self, ogrenciler,notlar,agirliklar):
        self.ogrenciler = ogrenciler
        self.notlar = notlar
        self.agirliklar = agirliklar

analiz = SinifAnalizi(ogrenciler, notlar, agirliklar)
print(analiz.ogrenciler)