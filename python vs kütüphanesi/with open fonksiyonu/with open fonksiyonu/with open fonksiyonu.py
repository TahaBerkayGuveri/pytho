with open("TextFile1.txt") as f:#bu programda proje sistemi var,yanitextfile1 i bulabilmesi i�in bu dosyaya sa� t�klay�p text dosyas�n� eklememiz laz�m.
    icerik=f.readlines()#�nce alta bak
    for satir in icerik:#burada ise readlinesta olan \n ile a�a�� iniyor sonra da print ile a�a�� iniyor,bu yuzden birer bo�luk b�rakarak yazd�r�r.
        print(satir)#bunu engellemek i�in 4.teste bak.

with open("TextFile1.txt")as f:#readlines ile yazd�rd���m�zda \n konarak liste olu�turur=>['jaelbnabn�OAN\n', 'PAJNP�wo�hn�wo\n', 'ajknbl�bnwf�']
    icerik=f.readlines()
    print(icerik)



f=open("TextFile1.txt")
icerik=f.read()
print(icerik)
f.close()


with open("TextFile1.txt") as f:#1.testin versiyonu bo�l�k b�rakmaz.
    icerik=f.readlines()
    for satir in icerik:
         print(satir,end="")
    print()#burada bir sonraki kod ile problem olu�uyor,textin 1.sat�r�n� bu kodun sonucunun 3.sat�r�na yan yana yazd�r�yor:bunu ��zmek i�in;
    #end de bo�luk b�rakmad�k ��nk� alt alta bo�luk b�rakmadan yazd�rmak istiyoruz.ama bu sefer sonraki kod ile debiti�ik yaz�l�yor yani bize bir \n laz�m
    #bunun i�in de varsay�ml� olarak gelen print i bo� b�rakarak yazd�rd�k yani for d�ng�s� bittikten sonra bir bo�luk b�rak�p alta ge�mesini s�yledik.
    #yani print i�ine girilen karakteri (bo�luk da olsa) yazd�r�p alta ge�er.



with open("TextFile1.txt") as f:#readline metodu ile sadece 1 sat�r� okur
    satir= f.readline()#.tell bize txt dosyas�ndaki imlcein ka��nc� sat�rda oldu�unu,.seek fonksiyonu ise imlecin istedi�imiz sat�ra d�nmesini sa�lar.!!!!!!
    print(satir)
    pozisyon=f.tell()
    print(pozisyon)


with open("TextFile1.txt")as f:
    satir= f.readline()
    print(satir)
    f.seek(0)#en ba�a d�nd� ve yeniden yazd�rd�.
    satir= f.readline()
    print(satir)


with open("TextFile1.txt")as f:#o dosyadan istenilen karakter say�s�ndaki karakterleri al�r.(i�ine say� girince)
    icerik=f.read(18)
    print(icerik)

with open("TextFile1.txt")as f:#her sat�r�n istenilen kadar�n� alma
    icerik=f.read(6)
    print(icerik)
    icerik=f.read(6)
    print(icerik)


with open("TextFile1.txt")as f:#ba�tan sekizer sekizer okur.o sat�r bitince alta ge�er=>#jaelbnabn�OAN                                                                                    
    icerik=f.read(8)                                                                    #PA
    print(icerik,end="")
    icerik=f.read(8)
    print(icerik,end="")
    print()

with open("TextFile1.txt")as f:#bu kod �sttekiler ayn� sonucu verir,ancak amac� dosyay� par�a par�a okumakt�r,yani uzun dosyalarda pc performans�n� art�rmak veya pc yi �ok yormamak i�in par�alara b�l�n�r
    okunacak_miktar=10             #!!!!!!
    icerik=f.read(okunacak_miktar)
    while len(icerik)>0:
        print(icerik,end="")
        icerik=f.read(okunacak_miktar)

#yazma moduyla olmayan dosyay� okumaya �al���rsak hata verir ancak w yani write moduyla olmayan dosyay� yazd�rmaya �al���rsak o dosyay� olu�turur.

with open("TextFile1.txt","w")as f:#dosyadakiler silinip yerine yaz�l�r.
    f.write("merhaba")
    

with open("TextFile1.txt","a")as f:#dosyadakilere yeni metin ekler.
    f.write("merhaba")              #dosyan�n i�indekiler silinmez.


with open("TextFile1.txt")as okunacak:#1.texti okur,3.texte yazd�r�r.
    with open("TextFile3.txt","w")as yazilacak:
        icerik=okunacak.readlines()#bu sat�r yerine for sat�r in okunacak: deyip alt�na yaz�lacak.write(sat�r) yazabiliriz.
        for satir in icerik:#readlines ile listeye �evirip for d�ng�s� ile yazd�rd�k.
            yazilacak.write(satir)

with open("alper copy.jpg","rb")as okunacak:#readbyte ve writebyte olarak kullan�l�r read ve write textlerde kullan�l�r.
    with open("python.jpg","wb")as yazilacak:
        okunacak_miktar=1024
        icerik=okunacak.read(okunacak_miktar)
        while len(icerik)>0:
            yazilacak.write(icerik)
            icerik=okunacak.read(okunacak_miktar)#while d�ng�s�n�n hatas�z �al��mas� i�in bu sat�r yaz�larak icerik dei�keni g�ncellenir.
#foto�raf� metni her neyse bu program�n oldu�u klas�re at.!!!!!!!!!!!!