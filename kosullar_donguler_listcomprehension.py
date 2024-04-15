# BOOLEAN   => 0: false, 0 haricindeki tüm değerler: true
# && = AND
# || = OR
# ! = NOT
# not 2==2  ve  !(2==2)   => false

listem = [1,2,3,4,5,6,7,8,9]
sayac=0
toplam=0
for eleman in listem:       # listedeki elemanların toplamı
    sayac+= 1
    toplam += eleman
print("toplam:",toplam)
print("döngü çalışma sayısı:",sayac)  # döngü 9 kere yani bütün elemanlar bitene kadar çalışmış.

s= "python"
for krk in s:
    print(krk*3,end="-") # araya - koyarak harfleri 3 kez yazdı. => ppp-yyy-ttt-hhh-ooo-nnn-

i=0
while (i<20):
    print("i'nin değeri",i)  # koşul sağlanana kadar dewam eder. çift sayıları yazdırır.
    i+=2               

a=0
while (a< len(listem)):
    print("indeks:",a,"eleman:",listem[a]) # liste üzerinde indeks ile gezinme.
    a+=1


# RANGE
range(0,20) # 0dan 20ye 20 dahil değil. sayı dizisi oluşturur.
print(*range(0,20))  # başına * ekleyince hepsini tek tek yazar.

lst= list(range(5,110,10))  # liste fonk ile range kullanımı. 5ten başla 110a kadar 10ar 10ar git ve liste oluştur.
print(lst)

for sayi in range(0,10):
    print(sayi)
    
for yldz in range(1,20):   # yarım çam ağacı oluşturdu.
    print("* " * yldz)

# BREAK  VE  CONTINUE

while True:
    isim = input("isminiz(çıkmak için q tuşuna basın.):")  
    if (isim == "q"):                # break yazılmazsa sonsuz döngüye girer.
        print("çıkış yapılıyor...")
        break
    print(isim)


bb= [1,2,3,4,5,6,7,8,9,10,11,12,13]

for i in bb:                  # 1den 10a kadar yazdırır 3 veya 5i es geç atla diyor.
    if(i==3 or i==5):
        continue
    print("i:",i)


j=0
while(j<10):
    if (j==2):
        j+=1     # continue dan sonra alttan +1 arttırmayı görmeyeceği için iki yere +1 ekledik.
        continue # böylece 0'ı da yazdırmış oluyoruz.
    print(j)
    j+=1

# LIST COMPREHENSION   -  input ile çoklu değer alma.

liste1 = [1,2,3,4,5]
liste2 = [i for i in liste1] # liste1'den ikinci listeyi oluşturuyoruz.
print(liste2)

liste3 = [1,2,3,4,5]
liste4 = [i*2 for i in liste3] # liste1'den ikinci listeyi oluşturuyoruz. (ama iki ile çarpımlarını) => [2, 4, 6, 8, 10]
print(liste4)

liste5 = [(1,2),(3,4),(5,6)]
liste6 = [k*z for (k,z) in liste5] # liste içinde tuple var ve tupleları çarpmamız istenmiş. => [2, 12, 30]
print(liste6)

liste7 = [1,2,3,4,5,6,7,8,9,10]    # eğer i 4 veya 9a eşit değilse o i'yi al iki katını liste 8'e ekle.
liste8 = [i*2 for i in liste7 if not (i==4 or i==9)]
print(liste8)             # => [2, 4, 6, 10, 12, 14, 16, 20]

g= "python"
liste9= [i*3 for i in g] # => ['ppp', 'yyy', 'ttt', 'hhh', 'ooo', 'nnn']
print(liste9)


