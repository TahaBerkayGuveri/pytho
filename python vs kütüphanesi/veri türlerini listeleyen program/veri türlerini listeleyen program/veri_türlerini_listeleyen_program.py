liste_methodlari=[]
for metod in dir(list):
    if metod.startswith("__"):
        continue
    else:
        liste_methodlari.append(metod)

demet_metodlari=[]
for metod in dir(tuple):
    if metod.startswith("__"):
        continue
    else:
        demet_metodlari.append(metod)

kume_metodlari=[]
for metod in dir(set):
    if metod.startswith("__"):
        continue
    else:
        kume_metodlari.append(metod)

sozluk_metodlari=[]
for metod in dir(dict):
    if metod.startswith("__"):
        continue
    else:
        sozluk_metodlari.append(metod)

string_metodlari=[]
for metod in dir(str):
    if metod.startswith("__"):
        continue
    else:
        string_metodlari.append(metod)

basliklar=["liste metodları","demet metodları","küme metodları","sözlük metodları","string metodları"]
siniflar=[liste_methodlari,demet_metodlari,kume_metodlari,sozluk_metodlari,string_metodlari]#listelerden oluşan bu listeyi döngülerde kullanmak için oluşturduk.

#önce en fazla elemana sahip listeyi bulalım ki elemanı az olanların listesinde aşagığa doğru ____ karakterleri yazdırılacak.
en_fazla_eleman=0
for sinif in siniflar:
    if len(sinif)>en_fazla_eleman:
        en_fazla_eleman=len(sinif)

for baslik in basliklar:#başlıkları yazdırdık.
    print(baslik,end="")
    print(" "*(30-len(baslik)),end="")


for i in range(en_fazla_eleman):
    print()#i her değiştiğinde alt satıra geçsin.
    for sinif in siniflar:
        if i>=len(sinif):
            print("______",end="")#alt satıra geçmesini engelledik.
            print(" "*24,end="")#her sütun 30 karakterden oluşacağı için bu kodu yazdık.
        else:
            print(sinif[i],end="")
            print(" "*(30-len(sinif[i])),end="")








