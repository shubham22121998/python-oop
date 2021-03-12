class Phone:
    def __init__(self,brand,price,camera):
        self.brand=brand
        self.price=price
        self.camera=camera
    def buy(self):
        print("buying a phone")
    def return_phone(self):
        print("retuen the phone")

class feature_phone:
    pass
class smart_phone:
    pass
Phone("SAMSUNG",35000,"12PX").buy()