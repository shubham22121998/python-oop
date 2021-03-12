class customer:
    def __init__(self,name,age,phone_no):
        self.name=name
        self.age=age
        self.phone_no=phone_no
    def purchase(self,payment):
        if payment.type=="card":
            print("payment by card")
        elif payment.type=="e-wallete":
            print("payment by e-wallet")
        else:
            print("some other option")

class payment:
    def __init__(self,type):
        self.type=type
payment1=payment("card")
c=customer("shubham",22,234433)
c.purchase(payment1)

