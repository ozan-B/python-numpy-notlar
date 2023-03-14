import numpy as np


##NUMPY ARRAY OLUŞTURMA  
"""Numpy içinde en önemli nesne ndarray adı verilen N boyutlu bir dizi türüdür. Python’ın standart veri tipi
 olan List çok esnek bir yapı kullanıyordu. Veri Yapılarındaki “Bağlı liste” veri yapısının bir versiyonu olan
 List içine farklı veri tipleri eklenebilir. Fakat, ndarray  aynı veri türüne ait bir yapıdır. Başka bir deyişle
 bellekte aynı boyutta ve sıralı verilerden oluşur. Aynı listede her verinin aynı veri tipi (dtype) vardır."""
 
ozan =np.array([1.23,3,4,5,9.22],dtype="int")
#print(ozan[0])

##sıfırdan array oluşturma
ozan2=np.zeros(10,dtype="int")

ozan3=np.ones((3,5))

ozan4=np.full((3,3),7)

ozan5=np.arange(0,37,3) # sıfırdan başla 37 ye kadar elemanları 3er 3er artan bir dizi oluştur

ozan6=np.linspace(0,1,5)

ozan7=np.random.normal(10,4,(3,4)) # ortalama,standartsapma,(matrix sayısı)

ozan8=np.random.randint(0,10,(3,3)) # elemanları 0 ve 10 arasında olan 3e 3lük bir matris oluştur.



##NUMPY ARRAY ÖZELLİKLERİ 

""" ndim  -> boyut sayısı
    shape ->boyut bilgisi 
    size  ->toplam eleman sayısı
    dtype ->array veri tipi """
    
    

print(ozan8.ndim) 

print(ozan8.shape) 

print(ozan8.size) 

print(ozan8.dtype)    


##YENİDEN ŞEKİLLENDİRME :reshape

ozan9= np.arange(1,10,1)

ozan9=ozan9.reshape((3,3)) # tek boyutlu diziyi 2 boyutluya dönüştürdüm başka deyişle tek boyutlu arrayi 2 boyutlu matrise dönüştürdüm.

##BİRLEŞTİRME (concatenate)


ozan10=np.array([1,2,3])
ozan11=np.array([4,5,6])

ozan12= np.concatenate([ozan10,ozan11])

#yukarıdaki tek boyutta birleştirme bir de 2 boyutlu birleştirmeyi deneyelim

ozan13=np.array([[10,20,30],
                 [40,50,60]]) #np.array ilede iki boyutlu matrisler oluşturulabilir burada ona bir örnek verdim

ozan14 =np.concatenate([ozan13,ozan13])

"""satır bazında değil sütun bazında birleştirmek için axis modülü kullanılır bu modül eksen belirtmek için kullanılır 
0 satırları 1 sütunları ifade eder yukarıdaki birleştirme işleminde axis değeri default olarak 0 dır"""
"""satır bazında birleştirmek alt alta birleştirmek demektir .Sütun bazında birleştirmek ise yan yana birleştirmek demeketir"""

ozan15 =np.concatenate([ozan13,ozan13],axis=1)



##Array Ayırma (split)

ozan16 = np.array([1,2,3,4,5,34,35,36])
ozan17 = np.split(ozan16,[3,5]) 
""" 2 ayırma işlemi verdiğimiz için 3 tane dizi oluşturuyor eğer 3 tane ayırma 
işlemi verseydik o zaman 4 tane yeni array oluştururdu. burada  3.indise kadar böl sonra 5.indise kadar böl
işlemi yapıyoruz"""

#böldüğümiz arrayleri nasıl bir eleman olarak kullanıcaz peki ? atama işlemini üç değişkene yapacağız

a,b,c= np.split(ozan16,[3,5])

# iki boyulu ayırma işlemini yapalım şimdi de


ozan18 = np.arange(16).reshape(4,4)#0dan16ya kadar değerler alan 4e 4lük bir array oluşturdum 

ust,alt=np.vsplit(ozan18, [2])  #2.satıra kadar olan kısmı ayırır dikey olarak

sag,sol=np.hsplit(ozan18, [2]) #2.sütuna olan kısmı ayırır düşey olarak 


# SIRALAMA (sort)

ozan19= np.array([2,1,3,4,3,5])

sırala=np.sort(ozan19)
"""NOT= eğer sort modiülü numpy kütüphanesinde çağırırsak (np.sort) ozan19 arrayinin orijinalinde bir değişiklik 
yapmayacaktır ancak sort modülünü dirtekt kullanırsak (ozan19.sort() işte o zaman ozan19 arrayinin orijinalinde
kalıcı bir değişiklik yapmış oluruz. """

#iki botulu array sıralama
ozan20= np.random.normal(20,5,(3,3))
sırala_ikili_satır= np.sort(ozan20,axis=1)  # satırlara göre sıralama
sırala_ikili_sütun= np.sort(ozan20,axis=0) # sütunlara göre sıralama


##Index ile elemanlara erişmek

ozan21= np.random.randint(10 , size=10)
ozan21[0] = 26 #tek boyutta eleman değiştirdim

ozan22= np.random.randint(10 , size=(3,5))
ozan22[0,1] = 55 # iki boyutta eleman değiştirdim

##ARRAY ALT KÜME İŞLEMLERİ(SLICE işlemleri)
ozan23= np.arange(20,30)

print(ozan23[0:2]) #0. - 2. indeklerinin arasındakini yazdır
print(ozan23[0::2]) #0.indexden başla  indekslerinin arasındakileri 2 şer 2şer atlayarak yaz

#şimdide iki boyutlu dizide deneyelim slice işlemlerini

ozan24= np.random.randint(10,size=(5,5))
print(ozan24[:,0]) #satırları gösterme ,0.sütunu göster
print(ozan24[0,:]) #0.satırı göster , sütunları gösterme  
print(ozan24[0:3,0:2]) # 0-3 satırları arasını al , oluşan tablonun tablonun 0-2. sütunları arasını yazdır


##ALT KÜME ÜZERİNDE İŞLEM YAPMAK
ozan25=np.random.randint(10 ,size=(5,5))

ozan25_a = ozan25[0:3 , 0:2].copy() 
"""seçilen alt kümeyi kopyalar bu kopya üzerinde işlemeler yaparsan ozan25 
                                        değişkeninin orijinalinde hiçbir değişklik olmamış olur."""
                                        
             
##FANCY INDEX İLE ELEMANLARA ERİŞMEK

ozan26=np.arange(0,30,3)
al_getir=[1,3,5]
print(ozan26[al_getir]) # ozan26 arrayinin 1.,2.,3. indislerinin yazdırır.

#İKİ BOYUTTA FANCY INDEX

ozan27= np.arange(0,20).reshape((4,5))

ozan27_satir =np.array([0,1])
ozan27_sutun =np.array([1,2])
print(ozan27_satir)
print(ozan27_sutun)
print(ozan27[ozan27_satir,ozan27_sutun])

##MATEMATİKSEL İŞLEMLER (numpy cheat sheet) kaynak->> https://web.itu.edu.tr/iguzel/files/Python_Cheat_Sheets.pdf
ozan28=np.array([1,2,3,4,5,6])

print(np.subtract(ozan28,1)) #dizinin her elemanını 1 eksiltir.
print(np.add(ozan28,1))      #dizinin her elemanına 1 ekler.
print(np.multiply(ozan28,5)) #dizinin her elemanını 5 ile çarpar.
print(np.divide(ozan28,5))   #dizinin her elemanını 5 'e böler.
print(np.power(ozan28,3))   #dizinin her elemanının 3.üssünü alır
print(np.mod(ozan28,2))     #dizinin her elemanının 2'ye bölümünden kalanları yazdır.  
print(np.absolute(np.array([-3]))) #dizinin elamanını mutlak değere alır.

##NumPy ile İki Bilinmeyenli Denklem Çözümü


""" 5* x0 + x1 =12
    x0 + 3 * x1 =10"""
    
a= np.array([[5,1],[1,3]]) # bilinmeyenlerin katsayıları
b= np.array([12,10])  #eşitliğin diğer tarafındakiler

x=np.linalg.solve(a,b)























