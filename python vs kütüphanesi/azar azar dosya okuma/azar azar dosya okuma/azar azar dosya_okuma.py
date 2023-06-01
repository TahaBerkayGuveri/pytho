with open("isimler ve notlar.txt",encoding="utf-8") as f:
    okunacak_miktar=10
    icerik =f.read (okunacak_miktar)
    while len(icerik)>0:
        print(icerik,end="")
        icerik=f.read(okunacak_miktar)
        #daha hýzlý okuma yapmak için bu þekilde yazdýk büyük dosyalarda tek seferde okumak zor olabilir.