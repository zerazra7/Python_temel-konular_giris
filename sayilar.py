x=10
y=4
k=70
z=x/y # // koyarsak tam sayı bölmesi yapar.
print("z=",z)
isim="azra"
print("Merhaba",isim,z)  # sen boşluk eklemesen bile otomatik olarak boşluk ekler.

print("x:",x,"y:",y)
x,y = y,x              #yerlerini değiştirdi.
print("x:",x,"y:",y) 

print("x:",x,"y:",y,"k:",k)
x,y,k= k,x,y           # 3lü olunca da çalışır.
print("x:",x,"y:",y,"k:",k)

z+=1     # 1 artırdık.
print(z)

sonuc= 2**5  # 2 üzeri 5 demek.
print(sonuc)
sonuc= 2**(1/5)  # 2 üzeri 0.2 demek.
print(sonuc)


