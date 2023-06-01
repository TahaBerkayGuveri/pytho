import math
def asal_bulucu(x):
    durum=True 
    if x%2==0:
        durum=False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            durum=False 
    return durum
toplam=0
for i in range(2,2000000):
    if asal_bulucu(i):
        toplam+=i 
print(toplam)