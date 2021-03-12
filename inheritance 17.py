#multi level inheritance
class Product:
    def review(self):
        print("customer give the review")
class Phone(Product):
    def __init__(self,brand,price,color):
        self.brand=brand
        self.price=price
        self.color=color
    def buy(self):
        print("customer by the mobile")
    def return_product(self):
        print("return the product")
class Smart_phone(Phone):
    def __init__(self,brand,price,color,os,ram,camera,rom):
        super().__init__(brand,price,color)
        self.os=os
        self.ram=ram
        self.camera=camera
        self.rom=rom
    def buy(self):
        print("buying a smart phone")
        super().review()
s=Smart_phone("appel",120000,"Red","ios","6GB","12MP","128GB")
s.buy()
