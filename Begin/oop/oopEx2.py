class Computer():
    name = "Monster"

    def __init__(self,kod,model,year,price):
        self.kod = kod
        self.model = model
        self.year = year
        self.price = price

    def __repr__(self):
        return "{} numaralı pc satılmıştır.".format(self.kod)

    def pc_bilgileri(self):
        return "{} {} kod numaralı {} modeli olan bilgisayar {} yılında çıkmıştır fiyatı da {} TL'dir.".format(
            self.name,
            self.kod,
            self.model,
            self.year,
            self.price
        )
    def fiyat_guncelleEksi(self,updatePrice):
        self.price -= updatePrice

    def fiyat_guncelleArti(self,updatePrice):
        self.price += updatePrice

computer1 = Computer(1,"Abra",2019,7200)
computer2 = Computer(2,"Tulpar",2018,9000)
print(computer1.pc_bilgileri())
print(computer2.pc_bilgileri())
computer1.fiyat_guncelleArti(1200)
print(computer1.pc_bilgileri())
print(computer2)