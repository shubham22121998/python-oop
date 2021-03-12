class mobile:
    def __init__(self,price,brand):
        print("inside the constractor",id(self))
        self.price=price
        self.brand=brand
    def return_product(self):
        print("inside the function",id(self))
        print("mobile brand is ",self.brand,"id of the object is",id(mob2))


mob1=mobile(1000,"apple")

mob2=mobile(2000,"samsung")

mob2.return_product()