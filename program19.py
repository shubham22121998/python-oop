class mobile:
    def __init__(self,price,brand):
        self.price=price
        self.brand=brand

mob1=mobile(1000,"apple")
mob2=mobile(2000,"samsung")
mob3=mobile(3000,"mi")

list_mobile=[mob1,mob2,mob3]

for i in list_mobile:
    print(i.price,i.brand)
