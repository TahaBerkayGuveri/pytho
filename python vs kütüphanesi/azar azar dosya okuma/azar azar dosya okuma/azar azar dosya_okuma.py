with open("isimler ve notlar.txt",encoding="utf-8") as f:
    okunacak_miktar=10
    icerik =f.read (okunacak_miktar)
    while len(icerik)>0:
        print(icerik,end="")
        icerik=f.read(okunacak_miktar)
        #daha h�zl� okuma yapmak i�in bu �ekilde yazd�k b�y�k dosyalarda tek seferde okumak zor olabilir.