class Car:
    def __init__(self,name ,price , color):
        self.name=name
        self.price=price
        self.color=color
    def buy(self):
        print("buy the car")
class Electric(Car):
    def __init__(self,name,price,color,avg,model,engin):
        super().__init__(name,price,color)
        self.avg=avg
        self.model=model
        self.engin=engin
    def buy(self):
        print("buy the eclectric car")
class non_electric(Car):
    def __init__(self,name,price,color,avg,model,engin):
        super().__init__(name,price,color)
        self.avg=avg
        self.model=model
        self.engin=engin
    def buy(self):
        print("buying non_electric car")
n=non_electric("BMW",2000000,"WHITE",20,"Q7","1.2l")
n.buy()