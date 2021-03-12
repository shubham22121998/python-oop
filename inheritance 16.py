#single inheritance
class phone:
    def __init__(self,brand,price,color):
        self.brand=brand
        self.price=price
        self.color=color
    def buy(self):
        print("customer by the phone")
    def return_phone(self):
        print("customer return the phone")
class smart_phone(phone):
    pass

s=smart_phone("appel",12000,"red")
s.buy()

