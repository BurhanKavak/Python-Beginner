class Account:
    def __init__(self,isim,soyisim,yas,bakiye):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.bakiye = bakiye

    def bilgiler (self):
        print("İsim : ",self.isim)
        print("Soyisim : ",self.soyisim)
        print("Yaş : ",self.yas)
        print("Bakiye : ",self.bakiye)

    def paraCek (self,miktar):
        if (self.bakiye - miktar < 0):
            print("Bakiyeniz yetersiz!!!")
        else:
            self.bakiye -= miktar
            print("Yeni bakiye : ",self.bakiye)

    def paraYatir(self,miktar):
        self.bakiye += miktar
        print("Yeni bakiye : ",self.bakiye)


account = Account("Burhan","Kavak",21,1000)
account.bilgiler()
account.paraCek(1000)
account.paraYatir(1200)

account.bilgiler()
