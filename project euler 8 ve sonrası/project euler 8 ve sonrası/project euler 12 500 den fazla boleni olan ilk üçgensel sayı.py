import math
def bolen_bulucu(x):
    bolen_sayisi=0
    for i in range(1,int(math.sqrt(x)+1)):#programý hýzlandýrmak için sadece kareköküne kadar olan sayýlara böldük sonra da kareköküne kadar olan sayýlardan bölünenleri
        if x%i==0:#alýp o sayýya böldük ve böylece diðer bölenleri de bulmuþ olduk yani özetle sadece kareköküne kadar olan sayýlarda bölünen sayýsýný alýp 2 ile çarptýk.
            bolen_sayisi+=1#bu yapýlan iþlem programý baya hýzlandýrmýþ oldu.
    return bolen_sayisi*2
a=1
while True: 
    ucgensel_sayi=(a*(a+1))/2
    if bolen_bulucu(ucgensel_sayi)>500:
        print(int(ucgensel_sayi))
        break
    a+=1





