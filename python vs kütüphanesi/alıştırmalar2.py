#girilen metindeki harflerin sayısını gösteren program
metin= input("Bir metin giriniz:")
Bir metin giriniz:bilgisayar
sozluk=dict()
for harf in metin:
    if harf in sozluk:
        sozluk[harf]+=1
    else:
        sozluk[harf]=1

        
for harf , adet in sozluk.items():
    print(harf,adet)




#girilen sayının tam kare olup olmadığını söyleyen program
sayı=int(input("Bir sayı giriniz:"))
Bir sayı giriniz:65
if int(karekok)==karekok:
    print(f"{sayı} sayısı bir tam karedir.")
else:
    print(f"{sayı} sayısı bir tam kare değildir.")


#append hatası append yerine metin2+="A" yazılır.
metin=input("Bir metin giriniz:")
Bir metin giriniz:alkadabra
metin2=""
for harf in metin:
    if harf=="a":
        metin2.append("A")
    else:
        metin2.append(harf)

        
Traceback (most recent call last):
  File "<pyshell#120>", line 3, in <module>
    metin2.append("A")
AttributeError: 'str' object has no attribute 'append'


#girilen metnin a harflerini büyüten program
metin=input("Bir metin giriniz:")
Bir metin giriniz:alkadabra
metin2=""
for harf in metin:
    if harf=="a":
        metin2+="A"
    else:
        metin2+=harf

        
print(metin2)
AlkAdAbrA


#bir başka yöntem (tam olmasa da)
metin=input("Bir metin giriniz:")
Bir metin giriniz:alkadabra
liste=list()
for harf in metin:
    if harf=="a":
        liste.append("A")
    else:
        liste.append(harf)

        
print(liste)
['A', 'l', 'k', 'A', 'd', 'A', 'b', 'r', 'A']





#bir başka yanlış yöntem(incelenmeli)
metin=input("Bir metin giriniz:")
Bir metin giriniz:alkadabra
for harf in metin:
    if harf=="a":
        print("A")
    else:
        print(harf)

        
A
l
k
A
d
A
b
r
A


