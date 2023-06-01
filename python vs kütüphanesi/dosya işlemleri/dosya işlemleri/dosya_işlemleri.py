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
    print()
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
            if ortalamalar[i]>=60:
                print(" "*17,end="")
                print("gecti",end="")
            else:
                print(" "*17,end="")
                print("kaldi",end="")
            i+=1
            print()    
        elif len(isimler)==3:#"" elemaný yüzünden liste 3 elemanlý oldu.
            print(isimler[0],end="")
            print(" "*(20-len(isimler[0])+1),end="")#boþluk karakterini +1 diye ekledik.
            print(tam_isim.split(" ")[-2],end="")
            print(" "*(21-len(soy_isim)),end="")#soy isim kýsmýndan dolayý ortalamalar bir karakter solda gözüküyordu bunun çözümü için 20 düzeltildi üstteki için de geçerli.
            print(ortalamalar[i],end="")
            if ortalamalar[i]>=60:
                print(" "*17,end="")
                print("gecti",end="")
            else:
                print(" "*17,end="")
                print("kaldi",end="")
            i+=1
            print()
    