sinir=999*999#bu klasik bir yöntem ama burada palindrom sayýlarda 3 basamaklý 2 sayýnýn çarpýmý olup olmadýðý kontrol edilmedi.
sinir1=100*100
palindrom_sayilar=[]
for i in range(sinir1,sinir+1):
    i=str(i)
    mekanizma=[]
    for basamak in i:
        mekanizma.append(basamak)
    mekanizma.reverse()#reverse ile listeyi tersine çevirip join ile listeyi stringe çevirdik ve palindrom olup olmadýðýný kontrol ettik.
    ters="".join(mekanizma)    
    ters=int(ters)
    i=int(i)
    if ters==i:
        palindrom_sayilar.append(i)
    else:
        continue
print(max(palindrom_sayilar))

palindrom_sayilar=[]#burada ise palindrom sayýlarýn 3 basamaklý 2 sayýnýn çarpýmý olup olmadýðý kontrol dilerek döngü kuruldu.
for i in range(900,1000):
    for k in range(900,1000):
        deneme=i*k
        deneme=str(deneme)
        mekanizma=[]
        for basamak in deneme:
            mekanizma.append(basamak)
        mekanizma.reverse()
        ters="".join(mekanizma)
        ters=int(ters)
        deneme=int(deneme)
        if ters==deneme:
            palindrom_sayilar.append(deneme)
        else:
            continue
print(max(palindrom_sayilar))
####her zaman deðiþkenlerin türüne yani str mi int mi olduðuna diikat et ve gerekli yerde imleç ile kontrol edip gerekli müdahaleleri yap.
#satýrlarýn döngülerde hangi bloklar içinde olmasý gerektiðini kafan içinde birkaç örnek ile uygulayýp bul
#döngü baþa döndüðünde tutulmasý gereken bilginin sýfýrlanýp sýfýrlanmadýðýna dikkat et.