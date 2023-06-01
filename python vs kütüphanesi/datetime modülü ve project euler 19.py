import datetime
bugun=datetime.date.today()
print(bugun)
#bu kodu şöyle de yazabiliriz:
from datetime import date
bugun=date.today()
print(bugun)
#bu algoritmaların mantığı (.kullanılan kısımların):büyük sınıftan küçük sınıfa gidilir yani sıralama yapılır.
#ilk kodda örneğin; datetime modülünün date sınıfının today fonksiyonunu kullanmuş olduk.

import datetime
bugun=datetime.date.today()
print(bugun)
print(bugun.day)
print(bugun.year)
print(bugun.month)
print(bugun.weekday())
#pazartesiyi 0dan başlatır bu yüzden haftanın kaçıcı günü olduğunu bir eksik yazdırır.
print(bugun.isoweekday())
#bu fonksiyonlarda parantez koymayın unutma!!!!


import datetime
bugun=datetime.date.today()
gecmis_tarih=date(2016,7,15)
print(gecmis_tarih)
print(gecmis_tarih.weekday())
print(type(gecmis_tarih))
#ekrana yazan string değildir <class 'datetime.date'> yazar yani tarih sınıfındadır.





from datetime import datetime
suan=datetime.now()
print(suan)
print(suan.ctime())
#bu satırda suan değişkeninde tarih belli olduğu için hata vermez ancak suan yerine datetime yazarsak hata verir çümkü ctime ın çalışacağı tarih belli değil.
#ctime zamanı daha düzenli yazdırır.





from datetime import datetime
suan=datetime.now()
print(datetime.strftime(suan,"%Y:%m:%d  %H"))
#veya
from datetime import datetime
suan=datetime.now()
print(suan.strftime("%Y:%m:%d  %H"))




#değişim için timedelta çağrılır,tarihi değişkene atayabilmek için datetime modülü çağrılır.
from datetime import datetime
from datetime import timedelta
suan=datetime.now()#datetime yerine date yazılırsa hata verir.
değişim=timedelta(days=7,hours=5,seconds=43)
print(suan+değişim)
print(suan-değişim)



#"1 ocak 1901den 31 aralık 2000e kadar kaç ayın ilk günü pazardır?"=>ilk project euler sorusu
pazar_sayısı=0
for yıl in range(1901,2001):
    for ay in range(1,13):
        if datetime(yıl,ay,1).weekday()==6:
            pazar_sayısı+=1
print(pazar_sayısı)            
#cevap 171 olarak karşımıza çıkar.
#4.satırda herhangi bir yılın herhangi bir ayının 1.gününün numarası 6 ise yani pazar ise demek istedik.
#4.satıra kesinlikle bakk!!!!!!!!!!!!!!!!!!!!!










