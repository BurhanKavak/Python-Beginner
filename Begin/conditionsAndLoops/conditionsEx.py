yas = 20

if yas < 18:
    print("Mekana giremezsiniz!")
elif yas == 18:
    print("Yaşınız tam 18 6.Aydan sonra girebilirsiniz!")
else:
    print("Mekana girebilirsiniz!")

x = int(input("X değerini giriniz : "))
y = int(input("Y değerini giriniz : "))
z = int(input("Z değerini giriniz : "))

"""Mantıksal operatörler 'and' 'or' 'not' şeklinde"""
if x > y and x > z:
    print("En büyük X")
elif y > x and y > z:
    print("En büyük Y")
else:
    print("En büyük Z")

liste = [1, 2, 3, 4]

for i in liste:
    print(i)

print("\n")
# range belirterek 20 den 32 ye kadar liste oluşturup 32 dahil değil sayıları tek tek yazıdırıyor.
for i in range(20, 32):
    print(i)

print("\n")
# yine range belirterek 0 dan 10 a kadar liste oluşturup yazdırıyoruz ama ikişer ikişer artarak yazdırıyoruz.
for i in range(0,10,2):
    print(i)