#from kullanırsak sadece kullanacağımız fonksiyonları seçeriz ve değişkene
#.lı şekilde metot uygulamayız.
from def_oluşturulmuş_fonksiyonlar import alan
sonuc=alan(2,4)
print(sonuc)

#değişkene .lı bir şekide dosyanın metotu uygulanır.
import def_oluşturulmuş_fonksiyonlar
sonuc=def_oluşturulmuş_fonksiyonlar.fonksiyon(6)
print(sonuc)



#def_oluşturulmuş_fonksiyonlar dosyası bir modüldür.Kendimiz modül oluşturduk.




#####oluşturulan modül ve yapılacak işlemin yazdığı (örnek olarak
#####def_oluşturulmuş_fonksiyonlar ve def_oluşturulmuş_fonksiyonlar2)dosyaları şimdilik aynı klasöre at,ilerde farklı klasörde olursa nasıl yapılacağı gösterilecek.



#Bu dosyayı kodlarda uzun uzadıya tekrar tekrar yazmak yerine kısaltabiliriz.
#as yapısı kullanarak yaparız
import def_oluşturulmuş_fonksiyonlar as dof
sonuc=dof.hacim(3,4,5)
print(sonuc)



