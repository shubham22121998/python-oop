#hierachicale inheritance

class Phone:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def buy(self):
        print("buying the phone")
    def return_product(self):
        print("return the product")
class feature_phone(Phone):
    pass
class smart_phone(Phone):
    pass
smart_phone("appel",230000).buy()