# metodlar hazır olur. fonksiyonları biz oluştururuz.

def selamla():
    print("hello world")

selamla()
print(type(selamla))

def faktoriyel(sayi):
    faktoriyel=1
    if (sayi == 0 or sayi==1):
        print("faktöriyel",faktoriyel)
    else:
        while (sayi > 1):
            faktoriyel*=sayi
            sayi-=1
        print("faktöriyel",faktoriyel)

faktoriyel(6)

"""def toplam(a,b,c):
    return a+b+c
def iki_kati(a):
    return a*2

tplm= toplam(30,4,5)
print(iki_kati(tplm)) """

def toplama (*p):   # * parametresi "kaç tane parametre alacağını bilmiyorum" anlamına gelir.
    toplam= 0      # değerelri toplar.
    print("parametreler:",p)
    for i in p:
        toplam+=i
    return toplam

def fonk():
    a=10          # yerel alanda bir değişken.
    print(a)

fonk()
#print(a)         a değişkeni yok oldu çünkü sadece yerelde çalışıyor.

d= 10
def fonks():
    global d   # fonksiyon içinde d nin değerini değiştirdik. artık 4 değerini benimsedi.
    d= 4       # if veya while içine değer atanırsa global değişken olur yerel değil. diğer dillerde farklıdır.
    print(d)

fonks() # => 4
print(d) # => 4

# LAMBDA fonksiyon yazımını kolaylaştırır.

ikiylecarp = lambda x : x * 2   # x parametremizi 2 ile çarp demek.
print(ikiylecarp(5))


def terscevir(s):
    return s[::-1]

print(terscevir("Zehra Azra Giray")) # => yariG arzA arheZ

ters= lambda y : y[::-1]
print(ters("Atatürk"))  # => krütatA

ciftmi= lambda sayi : sayi%2 == 0
print(ciftmi(88))   # => True

