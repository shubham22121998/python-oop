from abc import ABCMeta,abstractmethod
class Customer(metaclass=ABCMeta):
    def __init__(self,customer_name):
        self.__customer_name=customer_name
        self.bill_id=None
        self.bill_amount=None
    @abstractmethod
    def calculate_bill_amount(self):
        pass
    def get_customer_name(self):
        return self.__customer_name

    def show(self):
        pass

class OccasionalCustomer(Customer):
    __counter=1000
    def __init__(self,customer_name,distance_km):
        super().__init__(customer_name)
        OccasionalCustomer.__counter+=1
        self.bill_id="O"+str(OccasionalCustomer.__counter)
        self.__distance_km = distance_km

    def get_distance_km(self):
        return self.__distance_km

    def validate_distance_in_km(self):
        if (self.__distance_km>=1) and (self.__distance_km<=5):
            return True
        else:
            False
    def calculate_bill_amount(self):
        if self.validate_distance_in_km() is True:
            if self.__distance_km>1 and self.__distance_km<=2:
                dilivery_charge=5
                self.bill_amount=50*dilivery_charge

            elif self.__distance_km>2 and self.__distance_km<=5:
                dilivery_charge=7.5
                self.bill_amount=50*dilivery_charge

            else:
                self.bill_amount=-1
                return self.bill_amount
            return self.bill_amount
        else:
            return False

    def show(self):
        print("bill amount",self.bill_id,"name of customer",self.get_customer_name(),"bill amount",self.bill_amount)


class RegularCustomer(Customer):
    __counter=100
    def __init__(self,customer_name,no_of_tiffin):
        super().__init__(customer_name)
        RegularCustomer.__counter+=1
        self.bill_id="R"+str(RegularCustomer.__counter)
        self.__no_of_tiffin=no_of_tiffin

    def get_no_of_tiffin(self):
        return self.__no_of_tiffin

    def validate_no_tiffin(self):
        if self.__no_of_tiffin>=1 and  self.__no_of_tiffin<=7:
            return True
        return False


    def calculate_bill_amount(self):
        if self.validate_no_tiffin() is True:
            cos_of_tiffin=50
            self.bill_amount=cos_of_tiffin*7*self.__no_of_tiffin
            return self.bill_amount
        else:
            self.bill_amount = -1
            return self.bill_amount
    def show(self):
        print("bill amount",self.bill_id,"name of customer",self.get_customer_name(),"bill amount",self.bill_amount)



o= OccasionalCustomer("shubham",2)
o.calculate_bill_amount()
o.show()

r=RegularCustomer("ATUL",5)
r.calculate_bill_amount()
r.show()

o= OccasionalCustomer("KUNAL",4)
o.calculate_bill_amount()
o.show()


r=RegularCustomer("NIKHIL",7)
r.calculate_bill_amount()
r.show()


