veri=input("testler çalışsın mı?")



#TEST1
#çalışan program dosyasının yerini gösterir.=>getcwd fonksiyonu!!!!
import os
print(os.getcwd())




#TEST2
#bulunulan dosyayı değiştirip=>chdir ile  sonra da içinde bulunan klasörleri gösterdik yani listeledik=>listdir!!!!!
#içinde bulunan her şeyi listeler
import os
os.chdir("C:/Users/ALPER/Desktop/python kobay klasör")
print(os.listdir())



#TEST3
#listdir ile sadece bulunulan değil herhangi bir dosyanın içeriğini görüntüleyebiliriz.!!!!
import os
print(os.listdir("C:/Users/ALPER/Desktop/ALPER silme"))


#TEST4
#yan yana yazdırmak yerine for döngüsü ile alt alta yazdırabiliriz.direkt for döngüsünün içinde listeyi kullandık.
import os
for dosya in os.listdir("C:/Users/ALPER/Desktop/ALPER silme"):
    print(dosya)


#TEST5
#aynı sonucu veren farklı kullanım chdir ile dosyaya gidip sonra döngüyü yazdırdık
import os
os.chdir("C:/Users/ALPER/Desktop/ALPER silme")
for dosya in os.listdir():
    print(dosya)


#TEST6
#makedirs ile iç içe klasörleri oluşturabiliriz. ama önce chdir ile o dosyaya gitmemiz gerekli.   
if veri=="evet":
    import os
    os.chdir("C:/Users/ALPER/Desktop/ALPER silme")
    os.makedirs("denek2/denek3/denek4")


#TEST7
#mkdir ile yeni klasör oluşturabiliriz ama önce nereye yeni klasör oluşturacağımızı chdir ile söylemiş olduk.
#denek1 diye yeni dosya oluşturur.
#var olan dosyanın ismini yazamayız hata verir.
if veri=="evet":
    import os
    os.chdir("C:/Users/ALPER/Desktop/ALPER silme")
    os.mkdir("denek1")
#bu kod hatalı değil bu sayfayı çalıştırınca hata verecek çünkü denek1 adlı dosya zaten var o yuzden burayı kontrol için denek1i sil.
#makedirs birden fazla klasör oluşturur.mkdir tek klasör oluşturur.



##########TEST6 VE TEST7 DE ÖZEL DURUM OLDUĞU İÇİN (TEKRAR ÇALIŞMASI İÇİN DENEK1 VE DENEK2 SİLİNMELİ) İF YAPISI İLE ÇALIŞMALARI DENETLENDİ.


if veri=="evet":
#herhangi bir dosyanın içindeki dosyayı silmek için rmdir kullanılır.
    import os
    os.chdir("C:/Users/ALPER/Desktop/ALPER silme")
    os.rmdir("denek2")
#içinde boş da olsa klasör olan bir klasörü silmez.
#tamamen boş klaörü siler


#denek1i siler.ancak önce oluşturulması lazım. önceki testlerden bağımsız test
if veri=="evet":
    import os
    os.chdir("C:/Users/ALPER/Desktop/ALPER silme")
    os.rmdir("denek1")
#rmdir tek boş klasör siler, removedirs iç içe boş klasörleri siler.remove ise klasörü siler.!!!!!!!!!!!!!!!!!!!!!
########veriye evet yazılırsa üstteki kodlardan denek1 oluşur sonra bu kodla da silinir.


#mac os işletim sistemlerinde boş klasör listelendiğnde '.DS_Store'adlı gizli dosya oluşur,bunu kullanıcı göremez ama listelediğimizde görürüz.

#removedirs kullanımı!!!
if veri=="evet":
    import os
    os.chdir("C:/Users/ALPER/Desktop/ALPER silme")
    os.removedirs("denek2/denek3/denek4")

#remove da içine doğrudan adres alabilir;chdir ile içine gitmemize gerek yok
if veri=="evet":
    import os
    os.remove("C:/Users/ALPER/Desktop/ALPER silme/Oyunlar silme/American Truck Simulator.url")
#bu dosyayı sildi.

#!!!!!!!!!!!!!!
if veri=="evet":
    import os
    silinecek=os.listdir("C:/Users/ALPER/Desktop/ALPER silme")[9]
    os.remove("C:/Users/ALPER/Desktop/ALPER silme/"+silinecek)
#erişim engeli veriyor ancak kod doğrudur.
#listenin seçilecek dosyasını adrese yazdırır.


#dosyaya gidip bir dosyanın ismini değiştirmek için rename kullanılır. chdir kullanmadan oyunlar silme yerine tam adres yazılır.
if veri=="evet":
    import os
    os.chdir("C:/Users/ALPER/Desktop/ALPER silme")
    os.rename("Oyunlar silme","silinecek dosyalar")


#rename ile hem ismi hem de yerini değiştirebilriz.!!!!!!!!!!!
#alper silmenin içindeki silinecek dosyalar adlı dosyanın ismini silinecek dosyalar2 yapıp fare2 ye attık.
if veri=="evet":
    import os
    os.chdir("C:/Users/ALPER/Desktop/ALPER silme")
    os.rename("silinecek dosyalar","C:/Users/ALPER/Desktop/python kobay klasör/fare1/silinecek dosyalar2")
#1.sıraya hedef dosya konur,2.sıraya oluşmasını istediğimiz şeklini yazarız.


#chdir ile belirtilen adrese gidilip stat ile gidilen dosyadaki belirtilen dosyanın çeşitli özelliklerini görebiliriz.!!!!!!!!!!!!!!!!!!!!!!!!!
#.st_atime o dosyanın en son erişim zamanını gösterir.
import os
os.chdir("C:/Users\ALPER/Desktop/ALPER silme/Documents/American Truck Simulator")
print(os.stat("config.cfg").st_atime)

if veri=="evet":    
    import os
    from datetime import datetime
    os.chdir("C:/Users\ALPER/Desktop/ALPER silme/Documents/American Truck Simulator")
    zaman=os.stat("config.cfg").st_atime
    gerçek_zaman=zaman.ctime()
    print(gerçek_zaman)
#ctime float yani ondalıklı sayı almaz hat verir




#fromtimestamp ile saniye cinsinden verilen zamanı anlayabileyeceğimiz dilime çevirdik!!!!!!!!!!!!!!
import os
from datetime import datetime
os.chdir("C:/Users\ALPER/Desktop/ALPER silme/Documents/American Truck Simulator")
zaman=datetime.fromtimestamp(os.stat("config.cfg").st_atime)
print(zaman)


#.st_size boyutu yani büyüklüğü yazdırır.
#.st_mtime en son modifikasyon yani en son değiştirilme tarihini yazdırır(.st_atime gibi başlangıçtan şimdiye kadarki saniye cinsinden)



#BAK İSİM DEĞİŞTİRİRKEN ÖNCE CHDİR İLE GİT (BULUNDUĞUN DOSYA OLSA BİLE) AMA DEĞİŞTİRMEK İSTEDİĞİN KISIMDAN ÖNCESİNE KADARKİ KISMI YAZ.
#ÇÜNKÜ CHDİR İN MANTIĞI O DOSYAYA GİDER VE O DOSYANIN İÇİNDEKİLERE BAKAR SEN BURAYA PYTHON ALIŞTIRMA KODLAR I DA EKLERSEN PYTHON ALIŞTIRMA KODLAR DOSYASININ İÇİNDEN
#PYTHON ALIŞTIRMA KODLAR DİYE DOSYA ARAYACAK VE BULAMAYACAĞI İÇİN HATA VERECEK.
#BURAYA KESİNLİKLE BAK
if veri=="evet":
    import os
    os.chdir("C:/Users/ALPER/Desktop")
    os.rename("python alıştırma kodlar" ,"C:/Users/ALPER/Desktop/python kütüphanesi")

#########!!!!!!!!!!!!!    
import os
for geçerli_klasör,içindeki_klasör,içindeki_dosyalar in os.walk("C:/Users/ALPER/Desktop/python kütüphanesi"):
    print("geçerli klasör:",geçerli_klasör)
    print("içindeki klasör:",içindeki_klasör)
    print("içindeki dosyalar:",içindeki_dosyalar)
    print()

#programın çıktısı
#geçerli klasör: C:/Users/ALPER/Desktop/python kütüphanesi
#içindeki klasör: ['__pycache__']
#içindeki dosyalar: ['3 basamaklı sayılar ile küp koşulu.py', 'alıştırma kodlar 1.py', 'alıştırmalar2.py', 'datetime modülü strftime fonksiyonu notları.png', 'datetime modülü.py', 'def.py', 'def_oluşturulmuş_fonksiyonlar.py', 'def_oluşturulmuş_fonksiyonlar2.py', 'denemeler 1.py', 'fibonacci.py', 'hesap makinesi modülü.py', 'hesap makinesi.py', 'ilk 100 asal sayıdan koşullu program.py', 'kesinbak alıştırma hesap makinesi.py', 'modüller.py', 'os modülü.py', 'random modülü ve random fonksiyonu.py', 'time modülü.py']

#geçerli klasör: C:/Users/ALPER/Desktop/python kütüphanesi\__pycache__
#içindeki klasör: []
#içindeki dosyalar: ['def_oluşturulmuş_fonksiyonlar.cpython-310.pyc']
#####ilk önce adresteki klasörü geçerli klasör kabul eder,sonra içindeki klasörleri ve dosyaları yazdırır.
#####sonra adresteki klasörün içindeki klasörü geçerli klasör kabul edip içindeki dosyaları yazdırır.
#####peki program bunu nasıl anladı:klasörler dosyalara göre öncelikli!!!!çünkü dosyalarda klasörler üstte durur.



#önce klsöre gider,sonra onun içindeki klasörleri ve dosyaları yazdırır.sonra içindeki klasörlere teker teker geçip yine içindeki klasörlere ve edosyalara bakar. 
import os
for geçerli_klasör,içindeki_klasör,içindeki_dosyalar in os.walk("C:/Users/ALPER/Desktop/python kobay klasör"):
    print("geçerli klasör:",geçerli_klasör)
    print("içindeki klasör:",içindeki_klasör)
    print("içindeki dosyalar:",içindeki_dosyalar)
    print()

#path fonksiyonu !!!!!!!!!!!!!!!!!!!!!!!!#####
#stringlerde join metodu listelerdeki elemanların arasına istenilen bir karakter ile birleştiriyordu burada ise adres olarak birleştiriyor(os modülünde)
import os
os.chdir("C:/Users/ALPER/Desktop/python kobay klasör")
print(os.path.join("deneme1","deneme2","deneme3"))


import os
os.chdir("C:/Users/ALPER/Desktop/python kobay klasör")
print(os.path.join("deneme1","/deneme2","deneme3"))
#/ işaretinin olduğu yerden başlar,öncekileri görmez.


import os
os.chdir("C:/Users/ALPER/Desktop/python kobay klasör")
print(os.path.isfile("C:/Users/ALPER/Desktop/python kobay klasör/fare1/silinecek dosyalar2/Euro Truck Simulator 2.url"))
#isfile belirtilen adresteki nesnenin dosya olup olmadığını kontrol edip yazdıran
#isdir belirtilen adresteki nesnenin klasör olup olmadığını kontrol edip yazdıran


#splitext metodu da belirtilen adresteki dosyanın uzantısından adresi böler yani uzantıyı elde etmemizi sağlar.!!!!!!!!!!!!!!!
import os
os.chdir("C:/Users/ALPER/Desktop/python kobay klasör")
print(os.path.splitext("C:/Users/ALPER/Desktop/python kobay klasör/fare1/silinecek dosyalar2/Euro Truck Simulator 2.url"))







    

