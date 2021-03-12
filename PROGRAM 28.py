class Mobile:
    discount=50
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def purchase(self):
        total=self.price-self.price*Mobile.discount/100
        print(self.brand," with discounted price", total)
    @staticmethod
    def enable_discount():
        Mobile.set_discount(50)

    @staticmethod
    def disable_dicount():
        Mobile.set_discount(0)

    @staticmethod
    def get_discount():
        return Mobile.discount
    @staticmethod
    def set_discount(discount):
        Mobile.discount=discount
mob1=Mobile("appel",20000)
mob2=Mobile("samsung",300000)
mob3=Mobile("appel",200000)


Mobile.enable_discount()
mob1.purchase()
Mobile.disable_dicount()
mob2.purchase()
Mobile.enable_discount()
mob3.purchase()

