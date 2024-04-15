# elemanları değiştirilemeyen liste yapılarıdır. parantez ile kullanılır. (bkz: static list)
dmt=(5,)  
print(dmt) # tek elemanlı demet böyle oluşturulur.

demet=(1,1,2,3,4,5,6,7)
print(demet[4]) # = 4  (indekse ulaşma)
print(demet.count(1))  # aranan elemandan kaç tane olduğunu gösterir.
# dmt.index(4) 4 elemanının hangi insdexte olduğunu gösterir.
# replace fonksiyonuyla değişim yapılabilir fakat index ile erişilmez. 


# DICTIONARY
szlk=  {"sıfır":0,"bir":1,"iki":2,"denizli":20}
szlk2= dict() 
szlk3 = {}      # bu üç şekilde oluşturulabilir.

print(len(szlk))

szlk["sakarya"]= 54 # sözlüğe eleman ekleme.
print(szlk)

#iç içe sözlük yapısı döngülerde çok kullanılır.

print(szlk.values()) # değerleri verir. => dict_values([0, 1, 2, 20, 54])
print(szlk.items()) # elemanları verir. => dict_items([('sıfır', 0), ('bir', 1), ('iki', 2), ('denizli', 20), ('sakarya', 54)])



