# Değişken tanımlama
a = 3
b = 1.5
c = "Burhan"
d = [1, 2, 3, 4, 5, "Python"]
e = (1, 2, 3, 4, 5, "Python")
f = {"Elma": 3, "Armut": 2, "Muz": 4}
g = False

# Değişkenlerin tiplerini öğreniyoruz
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g),"\n")

x = 10
y = 12
print("Çarpım sonucu : ",x * y,"\n")


abc = "Selam olsun burdan bolu beyine"
liste = [1,2,3,4,5,6]

print("Uzunluk : ",len(abc),"\n")
print("Listenin son değerini : ",liste[len(liste) - 1],"\n")
print(abc[0:2]) # Burada 0 dan 2. indise kadar 2. değer dahil değil onları yazdırıyor.
print(liste[0:4]) # Burada 0 dan 4. indise kadar 2. değer dahil değil onları yazdırıyor.
print(liste[2:]) # Burada 2 den en sonuncu indise kadar 2. değer dahil değil onları yazdırıyor.
print(liste[:4]) # Burada baştan başla 4. indise kadar git 4. değer dahil değil.
print(liste[::2]) # Burada baştan başla sona kadar git ama ikişer ikişer ilerle.
print(abc[0:11:2]) # Burada baştan başla 11. indise kadar git ama ikişer ikişer ilerle diyoruz.
print("\n")


"""Bu kısımda stringi sayı ile çarpabiliyoruz."""
print("*" * 1)
print("*" * 2)
print("*" * 3)
print("*" * 4)
print("*" * 5)
