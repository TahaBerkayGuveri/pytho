

#burada for döngüsündeki sayı kısmı sting olmalıdır.İnteger olamaz.

Bir sayı giriniz:576
toplam=0
               
for rakam in sayı:
    toplam+=rakam

               
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    for rakam in sayı:
TypeError: 'int' object is not iterable


#girilen sayının rakamları toplamını veren program(burada rakam ifadesini toplama ekleyebilmek için rakam integere dönüştürülür.

sayı=input("Bir sayı giriniz:")
               
Bir sayı giriniz:567
toplam=0
               
for rakam in sayı:
    toplam+=int(rakam)

               
print(toplam)
               
18



#girilen sayının pozitif bölen sayısını gösteren program
sayı=int(input("Bir sayı giriniz:"))
Bir sayı giriniz:100
bolen_sayisi=0
for i in range(1,sayı+1):
    if sayı%i==0:
        bolen_sayisi+=1
        i+=1
    else:
        i+=1

        
print(bolen_sayisi)
9




#girilen sayının faktöriyelini hesaplayan program
sayı=int(input("Bir sayı giriniz:"))
Bir sayı giriniz:5
faktorıyel=1
for i in range(2,sayı+1):
    faktorıyel*=i
    i+=1

    
print(f"{sayı}!={faktorıyel}")
5!=120


#while döngüsü ile faktöriyel hesabı (başta i nin değeri atanmalı)
sayı=int(input("Bir sayı giriniz:"))
Bir sayı giriniz:5
i=1
faktorıyel=1
while i<=sayı:
    faktorıyel*=i
    i+=1

    
print(f"{sayı}!={faktorıyel}")
5!=120




#girilen sayının asal olup olmadığını kontrol eden ve yazdıran program *****kesinkle bak burada değişken verme yöntemi uyguladık.Değişkeni kullanarak döngü kurduk.
sayı=int(input("Bir sayı giriniz:"))
Bir sayı giriniz:43
değişken=True
for i in range(2,sayı):
    if sayı%i==0:
        değişken=False
        i+=1
    else:
        i+=1
        
if değişken==True:
    print(f"{sayı} sayısı asaldır.")
else :
    print(f"{sayı} sayısı asal değildir.")

    
43 sayısı asaldır.







#hesap makinesinin ilk adımı toplama işlemi tamamlandı:)
veri=int(input("Yapmak istediğiniz işlemi seçiniz:"))
Yapmak istediğiniz işlemi seçiniz:1
if veri==1:
    veri2=int(input("Kaç sayıyı toplayacaksınız?"))
    i=1
    toplam=0
    while i<=veri2:
        veri3=int(input("Sayı giriniz:"))
        toplam+=veri3
        i+=1
    print(toplam)

    
Kaç sayıyı toplayacaksınız?5
Sayı giriniz:3
Sayı giriniz:3
Sayı giriniz:3
Sayı giriniz:3
Sayı giriniz:4
16


