import math
def asal_bulucu1(x):
    durum=True
    if x%2==0:
        durum=False     
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            durum=False 
            return durum
    if durum:
        return x
def asal_bulucu2(x):
    atama=False
    for i in range(2,int(math.sqrt(x))+1):
        if type(asal_bulucu1(i))==int:
            if x%i!=0:
                atama=True
    return atama
        


sayi=5
toplam=5
while True:
    if asal_bulucu2(sayi):
        toplam+=sayi
    sayi+=1
    if sayi>=2000000:
        break
print(toplam)
    

