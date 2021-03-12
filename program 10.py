class Account:
    def __init__(self,name,age,account_number,balance):
        self.name=name
        self.age=age
        self.account_number=account_number
        self.__balance= balance
    def update_balance(self,amount):
        if amount<=1000 and amount>0:
            self.__balance+=amount
    def show_balance(self):
        print("current balance ",self.__balance)

c1=Account("shubham",22,1001,5000)
c1.update_balance(1000)
c1.show_balance()
print(c1.__balance)
