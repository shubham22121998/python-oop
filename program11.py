class customer:
    def __init__(self,custid,name,age,balance):
        self.custid=custid
        self.name=name
        self.age=age
        self.__balance=balance
    def set_update_account(self,amount):
        self.__balance+=amount
    def get_account_details(self):
        return self.__balance
c1=customer(1001,"shubham",22,5000)
c1.set_update_account(1000)
print(c1.get_account_details())