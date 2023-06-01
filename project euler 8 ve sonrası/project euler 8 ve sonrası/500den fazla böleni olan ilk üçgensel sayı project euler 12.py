#def bolen_sayisi(x):
#    bolenler=[]
#    for i in range(1,int(x)+1):
#        if x%i==0:
#            bolenler.append(i)
#    return len(bolenler)
#a=1
#b=2
#while True:
#    ucgensel=a*b/2   
#    if bolen_sayisi(ucgensel)>500:
#        print(ucgensel)
#        break
#    a+=1
#    b+=1



#project euler 16
sayi=2**1000
toplam=0
for i in str(sayi):
    i=int(i)
    toplam+=i
print(toplam)



