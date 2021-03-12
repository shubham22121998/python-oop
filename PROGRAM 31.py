class Example:
    counter=1000
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.mobile_id=Example.counter
        Example.counter+=1
mob1=Example("appel",200000)
mob2=Example("samsung",23000)

print("mon1",mob1.mobile_id)
print("mob2",mob2.mobile_id)
