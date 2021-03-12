class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.total_price=None
    def purchase(self):
        if self.brand=="apple":
            discount=10
        else:
            discount=5
        self.total_price=self.price-self.price*discount/100
        print("price of mobile",self.total_price,"for brand name is",self.brand)
    def return_product(self):
        print("refund for product ",self.total_price)
class Shoes:
    def __init__(self,material,price):
        self.material = material
        self.price=price
        self.total_price=total_price=None
    def purchase(self):
        if self.material=="leather":
            tax=5
        else:
            tax=2
        self.total_price=self.price+self.price*tax/100
        print("price of shoes",self.price,"brand name is",self.material)
    def return_product(self):
        print("refund of the product",self.total_price)

mob1=Mobile("apple",100000)
mob2=Mobile("samsung",50000)

shoe1=Shoes("leather",3000)
shoe2=Shoes("canvas",12000)

mob1.purchase()
mob2.purchase()

shoe1.purchase()
shoe2.purchase()

mob2.return_product()

shoe2.return_product()

import this