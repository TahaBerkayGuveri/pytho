#başlangıçtan girilen sayı ölçüsü kadar saniye ilerletir ve gelen tarihi yazdırır.
import time
zaman =time.ctime(10000000)
print(zaman)




#bu algoritmadaki başlangıç ve bitiş değişkenlerini yazmamızın nedeni bir programın çalışma süresini ölçmek
import time
baslangıc=time.time()
liste=[]
for i in range(10000000):#programın başı
    liste.append(i)#programın sonu
bitis=time.time()
print(bitis-baslangıc)


#localtime metodu tarihi farklı bir şekile yazdırır.İçine bir sayı girilirse üstteki gibi başlangıçtan girilen sayı kadar saniye ilerletir ve o tarihi yazdırır.
import time
zaman=time.localtime()
print(zaman)
    


#localtime fonksiyonu uygun bir formatta tarihi yazdırmaz ancak asctime fomksiyonu ile bu formatı anlayabileceğimiz formata dönüstürebilirz.
#localtime ı biz doğrudan belki kullsnmsysbiliriz ama bize gelen veri belki locsltime türündense bunu asctime ile çevirebiliriz.
import time
zaman=time.localtime(10000)
zaman2=time.asctime(zaman)
print(zaman2)



#straftime fonksiyonu ile zaman yazımını istediğimiz gibi düzenleyebiliriz.
import time
zaman =time.strftime("%d-%m-%Y %I:%M:%S %p")
print(zaman)




#programın belirli bir süre çalışmasını engeller.İçine girilen sayı kadar(saniye)
#örneğin bir sitenin tam yüklenmesini beklemek gibi(programın çalışması için)
import time
print("Program başlatıldı.")
time.sleep(4)
print("Program sonlandırıldı.")






