class customer:
    def __init__(self,name,age,phone_no):
        self.name=name
        self.age=age
        self.phone_no=phone_no
    def purchase(self,payment):
        if payment.type=="card":

class payment:
    def __init__(self,type):
        self.type=type
payment1=payment("caed")
c=customer()

