class  Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.discount=0
    def purchase(self):
        total_cost = self.price-self.price*self.discount/100
        print(self.brand,"original price is",self.price,"dicounted pice is",total_cost)
def enable_discount(list_of_item):
    for mobile in list_of_item:
        mobile.discount=50
def disable_discount(list_of_item):
    for mobile in list_of_item:
        mobile.discount=0



mob1=Mobile("APPEL",30000)
mob2=Mobile("SAMSUNG",45000)
mob3=Mobile("m1",3400)

list_of_item=[mob1,mob2,mob3]
enable_discount(list_of_item)
mob1.purchase()
disable_discount(list_of_item)
mob2.purchase()
mob3.purchase()
