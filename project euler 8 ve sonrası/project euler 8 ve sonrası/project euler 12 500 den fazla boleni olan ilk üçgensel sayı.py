import math
def bolen_bulucu(x):
    bolen_sayisi=0
    for i in range(1,int(math.sqrt(x)+1)):#program� h�zland�rmak i�in sadece karek�k�ne kadar olan say�lara b�ld�k sonra da karek�k�ne kadar olan say�lardan b�l�nenleri
        if x%i==0:#al�p o say�ya b�ld�k ve b�ylece di�er b�lenleri de bulmu� olduk yani �zetle sadece karek�k�ne kadar olan say�larda b�l�nen say�s�n� al�p 2 ile �arpt�k.
            bolen_sayisi+=1#bu yap�lan i�lem program� baya h�zland�rm�� oldu.
    return bolen_sayisi*2
a=1
while True: 
    ucgensel_sayi=(a*(a+1))/2
    if bolen_bulucu(ucgensel_sayi)>500:
        print(int(ucgensel_sayi))
        break
    a+=1





