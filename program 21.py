class  Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.discount=50
    def purchase(self):
        total_cost = self.price-self.price*self.discount/100
        print(self.brand,"original price is",self.price,"dicounted pice is",total_cost)
mob1=Mobile("APPEL",30000)

mob2=Mobile("SAMSUNG",45000)
mob3=Mobile("m1",3400)
mob1.purchase()
mob2.purchase()
mob3.purchase()
