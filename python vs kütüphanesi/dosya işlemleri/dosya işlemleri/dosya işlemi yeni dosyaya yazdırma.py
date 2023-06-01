def ortalama(liste):
    return sum(liste)/3
with open("isimler ve notlar.txt",encoding="utf-8") as hesaplayici:
    hesap=hesaplayici.readlines()#readlines ile listeye �evirdik.
    ortalamalar=[]
    for terim in hesap:
        kisi=str(terim)
        notlar=kisi.split(" ",3)[-1]#split stringi listeye b�ler.yani listeler olu�ur.4 par�aya k�sa olanlar da 3 par�aya yani olabilecek en �ok par�aya b�l�nd�.
        notlar=notlar.replace("\n","")#parantezdeki -1 en son terimi al�r ve bunu kisiye atam�� oluruz.
        notlar=notlar.split("/")#notlar� b�l�p liste olu�turduk.
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
        tam_isim=terim.replace( terim.split(" ",3)[-1] ,"")#replace metodunun kullan�m� buraya kesin bak!!!!!notlar� sildik.
        isimler=tam_isim.split(" ")
        soy_isim=tam_isim.split(" ")[-2]
        
        if len(isimler)==4:#"" karakteri y�z�nden liste 4 elemanl� oldu            
            print(isimler[0],isimler[1],end="")
            print(" "*(20-len(isimler[0]+isimler[1])),end="")
            print(soy_isim,end="")
            print(" "*(21-len(soy_isim)),end="")
            print(ortalamalar[i],end="")
            eokul.write(isimler[0])
            eokul.write(" ")
            eokul.write(isimler[1])
            eokul.write(" "*(20-len(isimler[0]+isimler[1])))#d�zen i�in 20 yerine 21 yap�ld�.
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

        elif len(isimler)==3:#"" eleman� y�z�nden liste 3 elemanl� oldu.
            print(isimler[0],end="")
            print(" "*(20-len(isimler[0])+1),end="")#bo�luk karakterini +1 diye ekledik.
            print(tam_isim.split(" ")[-2],end="")
            print(" "*(21-len(soy_isim)),end="")#soy isim k�sm�ndan dolay� ortalamalar bir karakter solda g�z�k�yordu bunun ��z�m� i�in 20 d�zeltildi �stteki i�in de ge�erli.
            print(ortalamalar[i],end="")
            eokul.write(isimler[0])
            eokul.write(" "*(20-len(isimler[0])+1))#bo�luk karakterini +1 diye ekledik.
            eokul.write(tam_isim.split(" ")[-2])
            eokul.write(" "*(21-len(soy_isim)))#soy isim k�sm�ndan dolay� ortalamalar bir karakter solda g�z�k�yordu bunun ��z�m� i�in 20 d�zeltildi �stteki i�in de ge�erli.
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

 #.write fonksiyonunda imle� mant��� vard�r ve print deki gibi i�ine end parametresi almaz.ayr�ca yaln�zca i�ine 1 parametre al�r.i�ine girilecek parametre de str olmak zorundad�r int olamaz.    
# PROJE TAMAMLANDI 



