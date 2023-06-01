#modüller:math
#tüm matematik modülünü yüklemek için böyle yazılır
import math
sonuc=math.factorial(5)
print(sonuc)

#burada factorial(sqrt(25)) yazılırsa hata verir.çünkü sqrt float olarak yani ondalıklı olarak döndürür,ondalıklı sayının faktoriyeli alınamaz.Bu yüzden arada integere
#çevrilir.
from math import factorial,sqrt
sonuc=factorial(int(sqrt(25)))
print(sonuc)


#yıldız ile yazılırsa yukarıdaki gibi sonrasında math modülü yazılmaz ama math modülündeki tüm fonksiyonlar yüklenebilir.
#abs yerine herhangi bir fonksiyon(sqrt,intifactorial vs.)yazılabilir.
from math import *
sonuc=abs(-56)
print(sonuc)




