import os
from datetime import datetime
def duzenle():
    klasor=input("Düzenlenecek klasör:")
    dosyalar=[]
    tarihler=[]
    def listemidir():
        for dosya in os.listdir(klasor):#!!!!listdir dosyanın içeriğini görüntülüyor.
            if os.path.isdir(os.path.join(klasor,dosya)):#join ile büyük klasör ile onun içindeki bir dosyayı veya klasörü birleştirerek yeni bir adres oluşturmuş olduk
                continue#isdir ile klasör olup olmadığını parantez içindeki kısım ile de adresi yazdırdık.
            if dosya.startswith("."):#gizli dosyaları engellemek için bu satırı yazdık
                continue
            else:
                dosyalar.append(dosya)
    listemidir()#listemidir fonksiyonunu çalıştırdık.
    for dosya in dosyalar:
        tarih_damgasi=os.stat(os.path.join(klasor,dosya)).st_ctime#.st lere dikkat et yazımı farklı.os.stat ile kullanılıyor.!!!!!!!
        tarih=datetime.fromtimestamp(tarih_damgasi).strftime("%d-%m-%Y")#datetime fromtimestamp strftime birlikte kullanımı tarihi oluşturup düzenliyor!!!!!!!
        if tarih in tarihler:
            continue
        else:
            tarihler.append(tarih)
    for tarih in tarihler:#oluşturacağımız dosyanın isminde başka dosya varsa diye kontrol ettik,yeniden oluşturulmasını engelledik
        if os.path.isdir(os.path.join(klasor,tarih)):
            continue
        else:
            os.mkdir(os.path.join(klasor,tarih))#mkdir ile yeni klasörümüzü oluşturduk.!!!!!
    for dosya in dosyalar:
        tarih_damgasi=os.stat(os.path.join(klasor,dosya)).st_ctime#aynı satır üstte de vardı ama döngü içindeydi o yüzden yeniden yazdık.
        tarih=datetime.fromtimestamp(tarih_damgasi).strftime("%d-%m-%Y")
        os.rename(os.path.join(klasor,dosya),os.path.join(klasor,tarih,dosya))#!!!!!!rename ile dosyanın yerlerini düzenledik
if __name__=="__main__":#bu kısım sonra öğrenilecek
    duzenle()
