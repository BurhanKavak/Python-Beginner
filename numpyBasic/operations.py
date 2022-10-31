import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2) # karesini alıyor

print(np.sqrt(9)) # Kök alma
print(np.sqrt(2)) # Karesini alma

# Matris çarpımı yapabilmemiz için a m  X m b olması gerekiyor.
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
y = np.array([[1,2,3],[4,5,6]])

print(x.dot(y.T),"\n") # .T yaparak transpozunu alıyoruz.

print("X matrisinin normal hali \n",x)


print("X matrisini vektörel hale yani yan yana hale getirme ",x.ravel())
print("\n")


z = np.random.random((2,3)) # 2'ye 3'lük random matrix oluşturuyor
print(z)
print(z.sum())
print(z.max()) # oluşan random matrixin max değerini veriyor.
print(z.min()) # oluşan random matrixin min değerini veriyor.

print(z.sum(axis=0)) # Column (sütunların toplamını veriyor)
print(z.sum(axis=1)) # Row (satırların toplamını veriyor)