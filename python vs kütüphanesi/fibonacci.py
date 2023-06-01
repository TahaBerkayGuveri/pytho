#fibonacci dizisinin ilk 100 elemanını yazdıram program
#while kısmına while len(fibonacci_list)==100: yazarsak hata verecektir çünkü while anlamı olduğu sürecedir.olana kadar değildir.
#burada while ile sonsuz döngü oluşturup bizim istediğimiz bir şart olunca durdurarak bir algoritma geliştirdik.
#6.satıra kesinlikle bak:listenin içindeki elemanları kullanarak ve değişken oluşturarak listeyi düzenledik.
fibonacci_list=list()
fibonacci_list.append(1)
fibonacci_list.append(1)
sony=2
while True:
    fibonacci_list.append(fibonacci_list[sony-2]+fibonacci_list[sony-1])
    sony+=1
    if len(fibonacci_list)==100:
        break
print(fibonacci_list)



#aynı şeyin for döngüsü ile yapımı
fibonacci_list=list()
fibonacci_list.append(1)
fibonacci_list.append(1)
sony=2
for i in range(2,100):
    fibonacci_list.append(fibonacci_list[sony-2]+fibonacci_list[sony-1])
    sony+=1
print(fibonacci_list)



#### Bu 2 kod ilk 100 fibonacci sayısını ekrana yazdrır.



#####len fonksiyonu int için kullanılamaz.
#100 basamaklı fibonaci sayısını ve kaçıncı eleman olduğunu ekrana yazdıran program
#100 basamaklı olup olmamasını değişken atayarak yaptık
fibonacci_list=list()
fibonacci_list.append(1)
fibonacci_list.append(1)
sony=2
while True:
    fibonacci_list.append(fibonacci_list[sony-2]+fibonacci_list[sony-1])
    sony+=1
    eleman=fibonacci_list[sony-2]+fibonacci_list[sony-1]
    eleman=str(eleman)
    if len(eleman)==100:
        print(eleman)
        break
print(sony)
    
####  DEĞİŞKEN ATA  ####














