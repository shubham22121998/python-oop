class Phone:
    def __init__(self,brand,price,camera):
        print("inside the phone constractor")
        self.brand=brand
        self.__price=price
        self.camers=camera
    def buy(self):
        print("buying mobile phone")
    def return_phone(self):
        print("return the phoine")
    def get_price(self):
        return self.__price
class Featuree_phone(Phone):
    def __init__(self,brand,price,camera,exchange):
        super().__init__(brand,price,camera)
        self.exchange=exchange
    def buy(self):
        print("buying feature phone")

class Smart_phone(Phone):
    def __init__(self,brand,price,camera,os,ram):
        super().__init__(brand,price,camera)
        self.os=os
        self.ram=ram
        print("inside the smart phone consractror")
    def buy(self):
        print("bupying smart phone")
s=Smart_phone("APPEL",120000,"12mp","ios","6GB")
s.return_phone()
print(s.get_price())

f=Featuree_phone("SAMSUNG",5000,"5MP","EXCHANGE ABLE")
f.buy()