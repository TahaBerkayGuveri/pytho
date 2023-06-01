import os
def seçici_uzantı():
    klasör=input("Düzenlenecek klasör:")
    dosyalar=[]
    uzantılar=[]
    def listemidir():
        for dosya in os.listdir(klasör):
            if os.path.isdir(os.path.join(klasör,dosya)):#join ile büyük klasör ile onun içindeki bir dosyayı veya klasörü birleştirerek yeni bir adres oluşturmuş olduk
                continue#isdir ile klasör olup olmadığını parantez içindeki kısım ile de adresi yazdırdık.
            if dosya.startswith("."):#gizli dosyaları engellemek için bu satırı yazdık
                continue
            else:
                dosyalar.append(dosya)
    listemidir()#listemidir fonksiyonunu çalıştırdık.
    for nesne in dosyalar:
        uzantı=nesne.split(".")[-1]#burada adresi uzantıdan önceki ve sonrakine göre noktayı kullanarak böldük ve 2.kısmı yani uzantıyı yani -1.nesneyi uzantıya atadık
        if uzantı in uzantılar:
            continue#aynı dosya türünden başka dosyalar da varsa yani daha önce eklendiyse listeye yine eklememek için bu kodu yazdık.
        else:
            uzantılar.append(uzantı)
    for uzantı in uzantılar:#oluşturacağımız dosyanın isminde başka dosya varsa diye kontrol ettik,yeniden oluşturulmasını engelledik
        if os.path.isdir(os.path.join(klasör,uzantı)):
            continue
        else:
            os.mkdir(os.path.join(klasör,uzantı))
    for dosya in dosyalar:
        uzantı=dosya.split(".")[-1]
        os.rename(os.path.join(klasör,dosya),os.path.join(klasör,uzantı,dosya))
if __name__=="__main__":#bu kısım sonra öğrenilecek
    seçici_uzantı()

            
