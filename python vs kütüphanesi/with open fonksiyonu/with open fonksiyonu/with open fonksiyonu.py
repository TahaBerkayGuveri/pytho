with open("TextFile1.txt") as f:#bu programda proje sistemi var,yanitextfile1 i bulabilmesi için bu dosyaya sað týklayýp text dosyasýný eklememiz lazým.
    icerik=f.readlines()#önce alta bak
    for satir in icerik:#burada ise readlinesta olan \n ile aþaðý iniyor sonra da print ile aþaðý iniyor,bu yuzden birer boþluk býrakarak yazdýrýr.
        print(satir)#bunu engellemek için 4.teste bak.

with open("TextFile1.txt")as f:#readlines ile yazdýrdýðýmýzda \n konarak liste oluþturur=>['jaelbnabnþOAN\n', 'PAJNPþwoýhnþwo\n', 'ajknblýbnwfþ']
    icerik=f.readlines()
    print(icerik)



f=open("TextFile1.txt")
icerik=f.read()
print(icerik)
f.close()


with open("TextFile1.txt") as f:#1.testin versiyonu boþlýk býrakmaz.
    icerik=f.readlines()
    for satir in icerik:
         print(satir,end="")
    print()#burada bir sonraki kod ile problem oluþuyor,textin 1.satýrýný bu kodun sonucunun 3.satýrýna yan yana yazdýrýyor:bunu çözmek için;
    #end de boþluk býrakmadýk çünkü alt alta boþluk býrakmadan yazdýrmak istiyoruz.ama bu sefer sonraki kod ile debitiþik yazýlýyor yani bize bir \n lazým
    #bunun için de varsayýmlý olarak gelen print i boþ býrakarak yazdýrdýk yani for döngüsü bittikten sonra bir boþluk býrakýp alta geçmesini söyledik.
    #yani print içine girilen karakteri (boþluk da olsa) yazdýrýp alta geçer.



with open("TextFile1.txt") as f:#readline metodu ile sadece 1 satýrý okur
    satir= f.readline()#.tell bize txt dosyasýndaki imlcein kaçýncý satýrda olduðunu,.seek fonksiyonu ise imlecin istediðimiz satýra dönmesini saðlar.!!!!!!
    print(satir)
    pozisyon=f.tell()
    print(pozisyon)


with open("TextFile1.txt")as f:
    satir= f.readline()
    print(satir)
    f.seek(0)#en baþa döndü ve yeniden yazdýrdý.
    satir= f.readline()
    print(satir)


with open("TextFile1.txt")as f:#o dosyadan istenilen karakter sayýsýndaki karakterleri alýr.(içine sayý girince)
    icerik=f.read(18)
    print(icerik)

with open("TextFile1.txt")as f:#her satýrýn istenilen kadarýný alma
    icerik=f.read(6)
    print(icerik)
    icerik=f.read(6)
    print(icerik)


with open("TextFile1.txt")as f:#baþtan sekizer sekizer okur.o satýr bitince alta geçer=>#jaelbnabnþOAN                                                                                    
    icerik=f.read(8)                                                                    #PA
    print(icerik,end="")
    icerik=f.read(8)
    print(icerik,end="")
    print()

with open("TextFile1.txt")as f:#bu kod üsttekiler ayný sonucu verir,ancak amacý dosyayý parça parça okumaktýr,yani uzun dosyalarda pc performansýný artýrmak veya pc yi çok yormamak için parçalara bölünür
    okunacak_miktar=10             #!!!!!!
    icerik=f.read(okunacak_miktar)
    while len(icerik)>0:
        print(icerik,end="")
        icerik=f.read(okunacak_miktar)

#yazma moduyla olmayan dosyayý okumaya çalýþýrsak hata verir ancak w yani write moduyla olmayan dosyayý yazdýrmaya çalýþýrsak o dosyayý oluþturur.

with open("TextFile1.txt","w")as f:#dosyadakiler silinip yerine yazýlýr.
    f.write("merhaba")
    

with open("TextFile1.txt","a")as f:#dosyadakilere yeni metin ekler.
    f.write("merhaba")              #dosyanýn içindekiler silinmez.


with open("TextFile1.txt")as okunacak:#1.texti okur,3.texte yazdýrýr.
    with open("TextFile3.txt","w")as yazilacak:
        icerik=okunacak.readlines()#bu satýr yerine for satýr in okunacak: deyip altýna yazýlacak.write(satýr) yazabiliriz.
        for satir in icerik:#readlines ile listeye çevirip for döngüsü ile yazdýrdýk.
            yazilacak.write(satir)

with open("alper copy.jpg","rb")as okunacak:#readbyte ve writebyte olarak kullanýlýr read ve write textlerde kullanýlýr.
    with open("python.jpg","wb")as yazilacak:
        okunacak_miktar=1024
        icerik=okunacak.read(okunacak_miktar)
        while len(icerik)>0:
            yazilacak.write(icerik)
            icerik=okunacak.read(okunacak_miktar)#while döngüsünün hatasýz çalýþmasý için bu satýr yazýlarak icerik deiþkeni güncellenir.
#fotoðrafý metni her neyse bu programýn olduðu klasöre at.!!!!!!!!!!!!