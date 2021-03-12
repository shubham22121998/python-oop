class Phone:
    def __init__(self,brand,price,camera):
        print("inside the constractor")
        self.brand=brand
        self.__price=price
        self.camera=camera
    def buy(self):
        print("buying the phone")
    def return_phone(self):
        print("return phone")

class feature_phone(Phone):
    pass
class smart_phone(Phone):

    def check(self):
        print(self.__price)

s=smart_phone("appel",12000,"12mpx")
s.check()