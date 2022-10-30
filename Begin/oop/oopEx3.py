class Product:

    def __init__(self, id, price, color):
        self.id = id
        self.price = price
        self.color = color

    def product_info(self):
        return "{} Id değerine sahip {} renkteki ürünümüz {} TL'dir.".format(self.id, self.color, self.price)


# Product'ı extends ediyor.
class Drink(Product):
    def __init__(self, id, price, color, tradeMark):
        super().__init__(id, price, color)
        self.tradeMark = tradeMark


product = Product(2, 4, "Beyaz")
print(product.product_info())

drink = Drink(5, 12, "Siyah","Kola")
print(drink.tradeMark)
