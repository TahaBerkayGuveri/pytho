#project euler 5
#problemde doðrudan ekok ifadesi yok biz yorum yaptýk , 20 sayýnýn hepsine bölünen en küçük sayý bunlarýn ekokudur.
import math
import functools
def ebob(x,y):
    return math.gcd(x,y)#ebob alan fonksiyon
def ekok(x,y):
    return math.lcm(x,y)#ekok alan fonksiyon
liste=range(1,21)
sonuc=functools.reduce(ekok,liste)#en baþtan 2sinini ekokunu alýr ayný yere yerleþtirir,sonra o ekok ile 3.nün ekokunu alýp yerleþtirir ,sonra onunla 4.nün ekokunu alýp yerleþtirir ve böyle devam eder.
print(sonuc)#böylece hýzlýca 20 sayýnýn ekoku alýnýr.

#project euler 9
for a in range(1,1000):
    for b in range(a,1000):
        c=1000-a-b #3.for döngüsü yazmak programý baya yavaþlatacaktýr
        if c>0:
            if c**2==(a**2+b**2):
                print(a*b*c)
                print(a,b,c)
                break
#project euler 9 vol/2
atama=True #çalýþýyor ancak çok uzun sürüyor.
while atama:
    for a in range(1,1000):
        for b in range(a,1000):
            for c in range(b,1000):#üsttekinebakýlýrsa bu 3. döngüye gerek yok çünkü elimizde toplamlarýnýn 1000 olmasý gibi bir bilgi var.
                if a+b+c==1000 and c**2==b**2+a**2:#buraya while yerine if yazdýk while ile döngü kurulmasýna gerek yok çünkü hem iþi uzatýrýz hem de döngüden çýkmak için yeni kodlar yazmamýz gerekir.
                    print(a*b*c)
                    atama=False 
                    break
#bir diðer yöntemin bir kýsmý
#def pisagor(x,y,z):
#    atama=True 
#    kare1=x**2
#    kare2=y**2
#    kare3=z**2
#    if x<y<z and sum(x,y,z)==1000 and kare3==(kare1+kare2):
#        return atama
#    if atama:
#        print(x*y*z)
#    else:
#        atama=False
#        return atama                    
               
                    

#project euler 7
#çalýþýyor ancak çok uzun sürüyor.
import math
def asal_bulucu(x):
    atama=True
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            atama=False 
            continue
    return atama    

asal_sayilar=[]
sayi=2
degisken=True 
while degisken:
    if asal_bulucu(sayi): 
        asal_sayilar.append(sayi)
    if len(asal_sayilar)==10001:
        degisken=False 
    sayi+=1
print(asal_sayilar[10000])





#project euler 3
import math
sayi=600851475143
def asalmidir(x):
    durum=True
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            durum=False 
            continue
    return durum
asal_bolen=[]
for i in range(2,int(math.sqrt(sayi))):
    if sayi%i==0 and asalmidir(i):
        asal_bolen.append(i)
print(max(asal_bolen))



