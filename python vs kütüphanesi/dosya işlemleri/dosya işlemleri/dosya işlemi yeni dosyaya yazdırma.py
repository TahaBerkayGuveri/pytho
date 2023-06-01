def ortalama(liste):
    return sum(liste)/3
with open("isimler ve notlar.txt",encoding="utf-8") as hesaplayici:
    hesap=hesaplayici.readlines()#readlines ile listeye çevirdik.
    ortalamalar=[]
    for terim in hesap:
        kisi=str(terim)
        notlar=kisi.split(" ",3)[-1]#split stringi listeye böler.yani listeler oluþur.4 parçaya kýsa olanlar da 3 parçaya yani olabilecek en çok parçaya bölündü.
        notlar=notlar.replace("\n","")#parantezdeki -1 en son terimi alýr ve bunu kisiye atamýþ oluruz.
        notlar=notlar.split("/")#notlarý bölüp liste oluþturduk.
        notlar2=[]
        for sayi in notlar:           
            sayi=int(sayi)
            notlar2.append(sayi)
        ortalamalar.append(int(ortalama(notlar2)))

with open("kalanlar ve gecenler.txt","w",encoding="utf-8")as eokul:
    basliklar=["isim","soy isim","ortalama","durum"]
    for baslik in basliklar:
        print(baslik," "*(20-len(baslik)),end="")
        eokul.write(baslik)
        eokul.write(" "*(21-len(baslik)))
    print()
    eokul.write("\n")
    i=0
    for terim in hesap:
        tam_isim=terim.replace( terim.split(" ",3)[-1] ,"")#replace metodunun kullanýmý buraya kesin bak!!!!!notlarý sildik.
        isimler=tam_isim.split(" ")
        soy_isim=tam_isim.split(" ")[-2]
        
        if len(isimler)==4:#"" karakteri yüzünden liste 4 elemanlý oldu            
            print(isimler[0],isimler[1],end="")
            print(" "*(20-len(isimler[0]+isimler[1])),end="")
            print(soy_isim,end="")
            print(" "*(21-len(soy_isim)),end="")
            print(ortalamalar[i],end="")
            eokul.write(isimler[0])
            eokul.write(" ")
            eokul.write(isimler[1])
            eokul.write(" "*(20-len(isimler[0]+isimler[1])))#düzen için 20 yerine 21 yapýldý.
            eokul.write(soy_isim)
            eokul.write(" "*(21-len(soy_isim)))
            eokul.write(str(ortalamalar[i]))
         
            if ortalamalar[i]>=60:
                print(" "*17,end="")
                print("gecti",end="")
                eokul.write(" "*19)
                eokul.write("gecti")
            else:
                print(" "*17,end="")
                print("kaldi",end="")
                eokul.write(" "*19)
                eokul.write("kaldi")
            i+=1
            print()
            eokul.write("\n")

        elif len(isimler)==3:#"" elemaný yüzünden liste 3 elemanlý oldu.
            print(isimler[0],end="")
            print(" "*(20-len(isimler[0])+1),end="")#boþluk karakterini +1 diye ekledik.
            print(tam_isim.split(" ")[-2],end="")
            print(" "*(21-len(soy_isim)),end="")#soy isim kýsmýndan dolayý ortalamalar bir karakter solda gözüküyordu bunun çözümü için 20 düzeltildi üstteki için de geçerli.
            print(ortalamalar[i],end="")
            eokul.write(isimler[0])
            eokul.write(" "*(20-len(isimler[0])+1))#boþluk karakterini +1 diye ekledik.
            eokul.write(tam_isim.split(" ")[-2])
            eokul.write(" "*(21-len(soy_isim)))#soy isim kýsmýndan dolayý ortalamalar bir karakter solda gözüküyordu bunun çözümü için 20 düzeltildi üstteki için de geçerli.
            eokul.write(str(ortalamalar[i]))
            if ortalamalar[i]>=60:
                print(" "*17,end="")
                print("gecti",end="")
                eokul.write(" "*19)
                eokul.write("gecti")
            else:
                print(" "*17,end="")
                print("kaldi",end="")
                eokul.write(" "*19)
                eokul.write("kaldi")
            i+=1
            print()
            eokul.write("\n")

 #.write fonksiyonunda imleç mantýðý vardýr ve print deki gibi içine end parametresi almaz.ayrýca yalnýzca içine 1 parametre alýr.içine girilecek parametre de str olmak zorundadýr int olamaz.    
# PROJE TAMAMLANDI 



