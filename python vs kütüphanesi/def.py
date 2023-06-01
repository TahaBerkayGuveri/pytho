def parazit(sayı1,sayı2,sayı3):
    return (sayı1%sayı2)//sayı3
sonuc=parazit(149,50,8)
print(sonuc)
#3 parametreli olarak tanımlanan fonksiyona 2 parametre girersek hata verir.
#hata vermesini istemiyorsak yani parametre girilmezse varsayılı olarak kabul edilmesini istiyorsak:
def parazit(sayı1,sayı2,sayı3=8):
    return (sayı1%sayı2)//sayı3
sonuc=parazit(149,50)
print(sonuc)
#3. parametre girilmezse tanım gereği 3.parametreyi 8 kabul etmesini söyledik.




#2.satırda return metin=metin.upper yazılırsa kod hata verir.return ifadesinin yanına değişken yazma,direkt yapılması gereken işlemi yaz.
def buyulten(metin):
    return metin.upper()
sonuc = buyulten("hacistoteles")
print(sonuc)




#metotlarda parantez koymayı unutma!!!
def buyulten(metin):
    metin=metin.upper()
    print(metin)
buyulten("hacistoteles")    



    
  
#parametreler str ise tırnağı unutma!
def selamla(isim):
    print(f"merhaba {isim}")
selamla("ali")


#fonksiyonun ismini değiştirebiliriz
def selamla(isim):
    print(f"merhaba {isim}")
fonk=selamla
fonk("ali")










