sinir=999*999#bu klasik bir y�ntem ama burada palindrom say�larda 3 basamakl� 2 say�n�n �arp�m� olup olmad��� kontrol edilmedi.
sinir1=100*100
palindrom_sayilar=[]
for i in range(sinir1,sinir+1):
    i=str(i)
    mekanizma=[]
    for basamak in i:
        mekanizma.append(basamak)
    mekanizma.reverse()#reverse ile listeyi tersine �evirip join ile listeyi stringe �evirdik ve palindrom olup olmad���n� kontrol ettik.
    ters="".join(mekanizma)    
    ters=int(ters)
    i=int(i)
    if ters==i:
        palindrom_sayilar.append(i)
    else:
        continue
print(max(palindrom_sayilar))

palindrom_sayilar=[]#burada ise palindrom say�lar�n 3 basamakl� 2 say�n�n �arp�m� olup olmad��� kontrol dilerek d�ng� kuruldu.
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
####her zaman de�i�kenlerin t�r�ne yani str mi int mi oldu�una diikat et ve gerekli yerde imle� ile kontrol edip gerekli m�dahaleleri yap.
#sat�rlar�n d�ng�lerde hangi bloklar i�inde olmas� gerekti�ini kafan i�inde birka� �rnek ile uygulay�p bul
#d�ng� ba�a d�nd���nde tutulmas� gereken bilginin s�f�rlan�p s�f�rlanmad���na dikkat et.