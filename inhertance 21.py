class Account:
    def account_type(self):
        print("valid account type")
    def balace(self):
        print("vald balance")
    def minimum(self):
        print("minimum")
class customer(Account):
    def __init__(self,customer_id,customer_name,age,account):
        self.customer_id=customer_id
        self.customer_name=customer_name
        self.age=age
        self.account=account
    def withdraw(self,amount):
        pass
    def take_card(self):
        pass
class privillage_customer(customer):
    def __init__(self,customer_id,customer_name,age,account,bonous_point):
        super().__init__(customer_id,customer_name,age,account)
        self.bonous_point=bonous_point
    def increase_bonous(self):
        pass
    def withdraw(self,amount):
        pass

