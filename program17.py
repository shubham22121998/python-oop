class shoes:
    def __init__(self,price,brand):
        print("inside the constractor",id(self))
        self.price=price
        self.brand=brand

mob1=shoes(1000,"apple")
print("mob1 id",id(mob1))

mob2=shoes(2000,"samsung")
print("mob2 id",id(mob2))