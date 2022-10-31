import pandas as pd

dictionary = {"İsim":["Burhan","Buse","Ayşenur","Yenes","Raşo"],
              "Yaş":[21,21,10,31,69],
              "Maaş":[250,100,0,50,200]}

dataFrame1 = pd.DataFrame(dictionary) # Bir execel dosyası gibi düzenli tablolandırma yapar.
print(dataFrame1)
print("\n")

head = dataFrame1.head(3) # Tablonun İlk 3 değeri alır default ilk 5 değer olarak karşımıza çıkar.
print(head)
print("\n")

tail = dataFrame1.tail(3) # Tablonun Son 3 değeri alır default son 5 değer olarak karşımıza çıkar.
print(tail)
print("\n")

print(dataFrame1.columns)
print("\n")
print(dataFrame1.info())
print("\n")

filtre1 = dataFrame1.Maaş > 100 # Filtreleme yapıyoruz burda maaşın 100 den fazla olanları getirmesini istiyoruz.
filtre2 = dataFrame1.Yaş < 30 # Filtreleme yapyıoruz burada yaşın 30 dan küçük olanları getirecek.
data = dataFrame1[filtre1 & filtre2] # Maaşı 100 den büyük yaşı da 30dan küçük değeri getirir.
print(data)