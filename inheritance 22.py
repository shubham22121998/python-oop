class parent:
    def __init__(self,brand,price):
        self.__brand=brand
        self.__price=price
    def show(self):
        print("show the method")
    def get_brand(self):
        return self.__brand
class child(parent):
    pass
c=child("s",12000)
print(c.get_brand())