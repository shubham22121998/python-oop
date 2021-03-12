class Customer:
    def __init__(self,customer_name,total_billamount):
        self.customer_name=customer_name
        self.total_bill_amount=total_billamount
    def  purchase(self):
        self.total_bill_amount=self.total_bill_amount-self.total_bill_amount*5/100
        return self.total_bill_amount

    def pay_bill(self,amount):
        print("name of customer",self.customer_name,"amount to be paid is :",self.total_bill_amount)


c1 =Customer("shubham",2000)
print(c1.purchase())
c1.pay_bill(c1.total_bill_amount)