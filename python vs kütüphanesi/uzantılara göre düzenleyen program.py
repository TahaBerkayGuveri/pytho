import os
klasör=input("Düzenlenecek klasör:")
def seçici_uzantı(adres):
    dosyalar=list()
    uzantılar=list()
    kobay_liste=list()
    for içindeki_dosyalar in klasör:
        kobay_liste.append(os.path.splitext(içindeki_dosyalar))
        dosyalar.append(kobay_liste[0])
        uzantılar.append(kobay_liste[1])
        kobay_liste.clear(0)
        kobay_liste.clear(1)           
    print(uzantılar)
    print(dosyalar)
seçici_uzantı(klasör)
