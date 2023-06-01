def bolen_toplami(x):
    bolen_toplam=0
    for i in range(1,x):
        if x%i==0:
            bolen_toplam+=i 
    return bolen_toplam
def dostane_sayi(x):
    dost=False
    sayi2=bolen_toplami(x)
    if sayi2==x:
        dost=False
        return dost
    if bolen_toplami(sayi2)==x:
        dost=True 
        return dost 

sonuc=0
for i in range(1,10000):
    if dostane_sayi(i):
        sonuc+=i
print(sonuc)
