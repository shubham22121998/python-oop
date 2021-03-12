class Customer:
    def __init__(self,customer_id,customer_name,address):
        self.__customer_id=customer_id
        self.__customer_name=customer_name
        self.__address=address
    def validate_customer_id(self):
        if len(str(self.__customer_id))==6 and str(self.__customer_id)[0]=='1':
            return True
        else:
            False
    def get_customer_id(self):
        return self.__customer_id
    def get_customer_name(self):
        return self.__customer_name
    def get_address(self):
        return self.__address


class Freight:
    counter=198
    def __init__(self,recipient_customer,from_customer,weight,distance):
        self.freight_id=Freight.counter+2
        self.recipient_customer=recipient_customer
        self.from_customer=from_customer
        self.weight=weight
        self.distance=distance
        self.freight_charge=None
        Freight.counter+=2
    def validate_weight(self):
        if self.weight%5==0:
            return True
        else:
            return False
    def validate_distance(self):
        if (self.distance >=500) and (self.distance<=5000):
            return True
        else:
            False
    def forward_cargo(self):
        if  self.from_customer and self.recipient_customer and self.validate_distance() and self.validate_weight():
            self.freight_charge=(self.distance * 60) + (self.weight * 150)
        else:
            self.freight_charge=1
    def get_freight_charge(self):
        return self.freight_charge
    def get_freight_id(self):
        return self.freight_id
    def get_recipinet_customer(self):
        return self.recipient_customer
    def get_from_customer(self):
        return self.from_customer
    def get_distance(self):
        return self.distance
    def get_weight(self):
        return self.weight
    def display(self):
        print(self.freight_id,self.freight_charge)

c1=Customer(123456,"shubham","indore")

f1=Freight(c1,123456,25,700)

c2=Customer(123678,"atul","indore")
f2=Freight(c2,c2,45,1400)
f1.forward_cargo()
f1.display()
f2.forward_cargo()
f2.display()


