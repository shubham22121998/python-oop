class mobile:
    discount=50 #static varible
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def purcahse(self):
        total_amount=self.price-self.price*mobile.discount/100
        print(self.brand,"  mobile orginal price is :" , self.price," discounted price is :",total_amount )
mob1=mobile("apple",120000)
mob2=mobile("samsung",50000)

mob1.purcahse()
mob2.purcahse()