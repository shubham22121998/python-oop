class Customer:
    def __init__(self,name,age,phone_no,address):
        self.name=name
        self.age=age
        self.phone_no=phone_no
        self.address=address
    def view_details(self):
        print(self.name,self.age,self.phone_no)
        print(self.address.door_no,self.address.street,self.address.area)
    def update_details(self,add):
        self.address=add
class Address:
    def __init__(self,door_no,street,area,pin_code):
        self.door_no=door_no
        self.street=street
        self.area=area
        self.pin_code=pin_code
    def view_details(self):
        pass
    def update_deatils(self):
        pass

add1=Address(101,"78","vijay nagar",452010)
add2=Address(1001,"54","vijay nagar",452010)

cust1=Customer("shubham",22,9893861208,add1)
cust2=Customer("ATUL",19,90909090,add2)

cust1.view_details()
cust1.update_details(add2)
cust1.view_details()