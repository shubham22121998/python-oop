class Phone:
    def __init__(self,brand,price,camera):
        print("inside the constractor")
        self.brand=brand
        self.__price=price
        self.camera=camera
    def buy(self):
        print("buying a phone")
    def return_phone(self):
        print("return the phone")
class smartphone(Phone):
    def buy(self):
        print("buying mobile")
        super().buy()
s=smartphone("samsung",12000,"12mp")
s.buy()

