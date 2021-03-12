#multiple inheritance
class Phone:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def buy(self):
        print("buying the phone")
    def return_product(self):
        print("return the product")
class Product:
    def review(self):
        print("give your review to product")
class smart_phone(Phone,Product):
    pass
s=smart_phone("appel",120000)
s.buy()
s.review()

'''
When a child is inheriting from multiple parents, and if there is a common behavior to be inherited, it inherits the method in 
Parent class which is first in the list. In our example, the buy() of Product is inherited as it appears first in the list
'''
print("---------------------------------------------------------------------------------")
class Phone:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def buy(self):
        print("buying the phone")
    def return_product(self):
        print("return the product")
class Product:
    def review(self):
        print("give your review to product")
class smart_phone(Product,Phone):
    pass
s=smart_phone("appel",120000)
s.buy()
s.review()