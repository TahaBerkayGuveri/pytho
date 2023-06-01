#3 basamaklı sayıların hangilerinin rakamlarının küplerine eşit olduğunu gösteren program
#bu algoritmadaki püf nokta sürekli olarak döngülerdeki değişkenlerin vs.türüne dikkat edip gerekli çevirmeleri yapmaktır.

liste=list()
for i in range(100,1000):
    toplam=0
    i=str(i)
    for basamak in i:
        basamak=int(basamak)
        x=basamak**3
        toplam+=x
    i=int(i)    
    if toplam==i:
        liste.append(i)

print(liste)       
        
        
#3 basamaklı sayıların hangilerinin rakamlarının küplerine eşit olduğunu gösteren program: 2.yol=>10a bölerek basamak bulma
#while döngüsünün içindeki geçici_sayı=geçici_sayı//10 kısmında tam bölüm yapılır, son kısımda ise örneğin 2 kalırsa 2nin 10a bölümü 0,xxx olacağı için geçici sayı=0 olur ve döngüden çıkılır.
#buradaki algoritma ise çift değişken atayarak döngü kurmaktır.Bu yönteme kesinlikle bak.
#burada çok dikkat edilmesi gereken bir nokta var:4.satırdaki anlama dikkat et.pythonda atama yani değişken okuma sağdan sola doğru yapılır.
#yani sayı=geçici_sayı yazarsak daha önceden geçici_sayı ifadesine bir şey atamadığımız için hata verir.Burada anlam şudur:geçici_sayı değerini sayı değişkenine ata
#yani geçici_sayı=sayı yazılır
liste=list()
for sayı in range(100,1000):
    toplam=0
    geçici_sayı=sayı
    while geçici_sayı!=0:
        basamak=geçici_sayı%10
        toplam+=basamak**3
        geçici_sayı=geçici_sayı//10
    if sayı==toplam:
        liste.append(sayı)
print(liste)















        
