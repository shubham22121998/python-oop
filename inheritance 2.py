class Phone:
    def __init__(self,brand,price,camera):
        self.brand=brand
        self.price=price
        self.camera=camera
    def buy(self):
        print("buying the phone")
    def return_phone(self):
        print("return phone")
class feature_phone(Phone):
    pass
class smart_phone(Phone):
    pass
Phone("appel",120000,"24mpx").return_phone()