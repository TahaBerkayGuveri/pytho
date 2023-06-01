#hesap makinesi hahahahahahah
#1:toplama
#2:çıkarma
#3:çarpma
#4:bölme
#5:karesini alma
veri=int(input("Yapmak istediğiniz işlemi seçiniz:"))
if veri==1:
    veri2=int(input("Kaç sayıyı toplayacaksınız?"))
    i=1
    toplam=0
    while i<=veri2:
        veri3=int(input("Sayı giriniz:"))
        toplam+=veri3
        i+=1
    print(toplam)
elif veri==2:
    c1=int(input("1.sayıyı giriniz:"))
    c2=int(input("2.sayıyı giriniz:"))
    sonuc=c1-c2
    print(sonuc)
elif veri==3:
    i=1
    sonuc=1
    veri4=int(input("Kaç sayıyı çarpacaksınız:"))
    while i <=veri4:
        veri5=int(input("Sayıyı giriniz:"))
        sonuc*=veri5
        i+=1
    print(sonuc)
elif veri==4:
    b1=int(input("1.sayıyı giriniz:"))
    b2=int(input("2.sayıyı giriniz:"))
    sonuc=b1/b2
    print(sonuc)
elif veri==5:
    x1=int(input("1.sayıyı giriniz:"))
    x2=int(input("2.sayıyı giriniz:"))
    sonuc=x1**x2
    print(sonuc)
