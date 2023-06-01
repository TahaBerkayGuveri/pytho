#project euler 5
#problemde do�rudan ekok ifadesi yok biz yorum yapt�k , 20 say�n�n hepsine b�l�nen en k���k say� bunlar�n ekokudur.
import math
import functools
def ebob(x,y):
    return math.gcd(x,y)#ebob alan fonksiyon
def ekok(x,y):
    return math.lcm(x,y)#ekok alan fonksiyon
liste=range(1,21)
sonuc=functools.reduce(ekok,liste)#en ba�tan 2sinini ekokunu al�r ayn� yere yerle�tirir,sonra o ekok ile 3.n�n ekokunu al�p yerle�tirir ,sonra onunla 4.n�n ekokunu al�p yerle�tirir ve b�yle devam eder.
print(sonuc)#b�ylece h�zl�ca 20 say�n�n ekoku al�n�r.

#project euler 9
for a in range(1,1000):
    for b in range(a,1000):
        c=1000-a-b #3.for d�ng�s� yazmak program� baya yava�latacakt�r
        if c>0:
            if c**2==(a**2+b**2):
                print(a*b*c)
                print(a,b,c)
                break
#project euler 9 vol/2
atama=True #�al���yor ancak �ok uzun s�r�yor.
while atama:
    for a in range(1,1000):
        for b in range(a,1000):
            for c in range(b,1000):#�sttekinebak�l�rsa bu 3. d�ng�ye gerek yok ��nk� elimizde toplamlar�n�n 1000 olmas� gibi bir bilgi var.
                if a+b+c==1000 and c**2==b**2+a**2:#buraya while yerine if yazd�k while ile d�ng� kurulmas�na gerek yok ��nk� hem i�i uzat�r�z hem de d�ng�den ��kmak i�in yeni kodlar yazmam�z gerekir.
                    print(a*b*c)
                    atama=False 
                    break
#bir di�er y�ntemin bir k�sm�
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
#�al���yor ancak �ok uzun s�r�yor.
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



