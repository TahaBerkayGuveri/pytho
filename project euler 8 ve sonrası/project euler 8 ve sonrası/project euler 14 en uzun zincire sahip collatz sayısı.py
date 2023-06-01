def collatz(x):
    zincir=1
    while True:
        if x==1:
            return zincir
        else:
            if x%2==0:
                x=x/2
                zincir+=1
            else:
                x=x*3+1
                zincir+=1
deger=0 
sonuc=0 
for i in range(1,1000000):
    if collatz(i)>sonuc:
        sonuc=collatz(i)
        deger=i
print(deger)



######diðer yol yapýlacak unutma sözlük kullanarak iþlemi hýzlandýracagýz ayný sayýlar zincirde denk gelirse onlarýn deðerleri direkt eklenerek iþlem yapýlmayacak.
collatz_sayilar=dict()
def collatz2(x):
    zincir=1
    if not x in  collatz_sayilar:
        collatz_sayilar[x]
