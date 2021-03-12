class Mobile:
    __discount=50
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def purchase(self):
        total=self.price-self.price * Mobile.__discount/100
        print("total price after discount",total)
    @staticmethod
    def get_discount():
        return Mobile.__discount
    @staticmethod
    def set_discount(discount):
        Mobile.__dicount=discount
mob1=Mobile("apple",20000)
mob2=Mobile("SAMSUNG",45000)

print(Mobile.get_discount())
#call get method using static method