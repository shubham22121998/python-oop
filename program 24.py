# static varible acces with the object
class mobile:
    __discount=50
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def purchase(self):
        total=self.price-self.price*mobile.__discount/100
        print("total price",total)

    def get_discount(self):
        return mobile.__discount

    def set_discount(self,discount):
         mobile.__discount = discount

mob1=mobile("apple",20000)
mob2=mobile("samsung",30000)
mob1.purchase()
mob2.purchase()
print(mob2.get_discount())