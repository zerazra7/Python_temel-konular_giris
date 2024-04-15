print("blablabla")
# arraylerden farkı farklı veri tiplerini bir arada bulundurabiliyor

#bir stringi listeye çevirebiliriz;
s="merhabalar"
lst=list(s)
print(lst)

#listelerde saymaya sıfırdan başlanır
alist=[1,2,3,4,5,6,7,8]
print(alist[2])  # =3

alist=alist+[9]  # listeye ekleme yaptık
print(alist)     # liste.append sonuna ekleme yapar.

alist[:2]= [40,50] #ilk iki elemanı değiştirdik.
print(alist) 

alist[-1]= [90] # son elemanı değiştirdik.
print(alist) 

# liste * 3 => listeyi 3 kere tekrar eder ( yazar )

# liste.pop()  index no verilmezse listedeki son elemanı siler.
# silinen = liste.pop(3) dersek silinen değeri gösterir. neyi sildiğimizi görmüş oluruz.

# liste.sort küçükten büyüğe sıralar.
# liste.sort(reverse = yes) büyükten küçüğe sıralar. str int karışık bi liste ise hata verir

ybs=[1,17,7,27,"pau","zz"]
print(ybs)
yeni_ybs = ybs[:3]    # listenin içinden yeni liste oluşturduk.
print(yeni_ybs)

icice= [alist,ybs,yeni_ybs] # iç içe liste oluşturuk.
print(icice)

