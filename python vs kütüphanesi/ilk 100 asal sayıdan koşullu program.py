#break kısmı sadece oradaki for döngüsünü bitirir,aşağıdaki kısım çalışmaya devam eder.
#burada çok işlem olur.Daha pratik ve şık bir yöntem daha var ki bu programın sonuç
#vermesi daha kısa sürer.Bir sayının asal olup olmadığını anlamak için kareköküne
#kadar olan sayılara bölmek yeterlidir.(karekökü de dahil)
#bir sayı karekökünden küçük sayılara bölünmüyorsa büyüklere de bölünmez.



liste=list()
liste.append(2)
sayı=3
while True:
    değişken=True
    for i in range(2,sayı):
        if sayı%i==0:
            değişken=False
            break
    if değişken==True:
        liste.append(sayı)
        if len(liste)==100:
            break
    sayı+=1

liste2=list()
for eleman in liste:
    eleman=str(eleman)
    if eleman.startswith("3") and eleman.endswith("7"):
        liste2.append(eleman)
print(liste2)        


#değişken atama ve bunu döngüde değiştirme yöntemi kullandık.
#break fonksiyonunun amacı döngüden çıkmak yani for döngüsünü bitirir.
