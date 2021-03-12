class Mobile:
    def __init__(self,brand,case):
        self.brand=brand
        self.case=case
    def display(self):
        print(self.case.color)
class case:
    def __init__(self,color):
        self.color=color
c1=case("white")
c2=case("black")
m1=Mobile("samsung",c1)
c1.color="black"
m1.display()