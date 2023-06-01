#random fonksiyonu  0 ile 1  arasında rastgele sayılar üretir.
import random
for i in range(1,11):
    print(random.random())



#######yazı tipini kurcala




#randint fonksiyonu da girilen 2 sayı arasında (2sınır da dahil) sayı üretir.
#randrange fonksiyonunda da 3 sayı girilir ,2.sınır dahil değildir ve atlayarak sayı üretir.
    
import random
for i in range(1,11):
    print(random.randrange(1,10,3))
    


#choice fonnksiyonu da bir liste içerisinde rastgele bir elemanı döndürür.
import random
liste=["siyah","beyaz","yeşil","sarı","gri","mavi"]
sonuc=random.choice(liste)
print(sonuc)
    

#shuffle fonksiyonu da listeyi karıştırır ama doğrudan sonuç üretmez.
#yani:
import random
liste=["siyah","beyaz","yeşil","sarı","gri","mavi"]
sonuc=random.shuffle(liste)
print(sonuc)
#yazılırsa none ifadesi karşımıza çıkar Bu yüzden direk ara satıra değiştirme satırı olarak eklenir.


import random
liste=["siyah","beyaz","yeşil","sarı","gri","mavi"]
random.shuffle(liste)
print(liste)




#sample fonksiyonu da parametre olarak içine bir liste alır ve o listenin içinden söylenen kadar elemanı seçer.(rastgele)
import random
liste=["siyah","beyaz","gri","yeşil","mavi","sarı"]
sonuc=random.sample(liste,3)
print(sonuc)




#sözlüklerdeki değerleri döngü kullanarak değiştirme
#5.satırda sözlükteki bir değeri değiştirme
#6.satırdaki zar ifadesi sözlükteki key lerin(1,2,3,,4,5,6)yerine geçer.sozluk[zar] ifadesi de o ifadenin sözlükteki değerini yazdırır.köşeli parantezi unutma.
import random
sozluk={1:0,2:0,3:0,4:0,5:0,6:0}
for i in range(100):
    zar =random.randint(1,6)
    sozluk[zar]+=1
for zar in sozluk:
    print(f"{zar}gelme olasılığı:{sozluk[zar]/100}")

#6 defa 5-5 gelmesi için yapılmsı gereken deneme sayısını ekrana yazdıran program
bes_bes=0
deneme_sayısı=0
while True:
    deneme_sayısı+=1
    zar1=random.randint(1,6)
    zar2=random.randint(1,6)
    if zar1==5 and zar2==5:
        bes_bes+=1
    if bes_bes==6:
        print(deneme_sayısı)
        break
    









