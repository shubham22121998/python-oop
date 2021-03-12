class Phone:
    def __init__(self,brand,price,camera):
        print("inside t5he constractor")
        self.brand=brand
        self.__price=price
        self.camera=camera
    def buy(self):
        print("buying the phone")
    def return_phone(self):
        print("return the product")
class feature_phone(Phone):
    pass
class smartphone(Phone):
    def __init__(self,os,ram):
        self.os=os
        self.ram=ram
        print("inside the smart phone constractor")
    def buy(self):
        print("buying the smart phone")

s=smartphone("ios",6)
s.buy()

