class Customer:
    def __init__(self,name,age,phone_no,address):
        self.name=name
        self.age=age
        self.phone_no=phone_no
        self.address=address
    def view_details(self):
        print(self.name,self.age,self.phone_no)
        print(self.address.get_door_no(),self.address.get_street(),self.address.get_area())
    def update_details(self,add):
        self.address=add
class Address:
    def __init__(self,door_no,street,area,pin_code):
        self.__door_no=door_no
        self.__street=street
        self.__area=area
        self.__pin_code=pin_code
    def get_door_no(self):
        return self.__door_no
    def get_street(self):
        return self.__street
    def get_area(self):
        return self.__area
    def get_pin_code(self):
        return self.__pin_code
    def set_door_no(self,value):
        self.__door_no=value
    def set_street(self,value):
        self.__street=value
    def set_area(self,value):
        self.__area=value
    def set_pin_code(self,value):
        self.__pin_code=value
    def update_deatils(self):
        pass

add1=Address(101,"78","vijay nagar",452010)
add2=Address(1001,"54","vijay nagar",452010)

cust1=Customer("shubham",22,9893861208,add1)
cust2=Customer("ATUL",19,90909090,add2)

cust1.view_details()
cust1.update_details(add2)
cust1.view_details()