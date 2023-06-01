import math
sonuc=math.factorial(100)
sonuc=str(sonuc)
toplam=0
for basamak in sonuc:
    basamak=int(basamak)
    toplam+=basamak
print(toplam)
