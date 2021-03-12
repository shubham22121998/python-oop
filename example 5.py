class OverdrawException(Exception):
    pass
class LimitreachedException(Exception):
    pass
class customer:
    def __init__(self,customer_id,customer_name,age,account):
        self.__customer_id=customer_id
        self.__customer_name=customer_name
        self.__age=age
        self.__account=account
    def get_customer_id(self):
        return self.__customer_id
    def get_customer_name(self):
        return self.__customer_name
    def get_age(self):
        return self.__age
    def get_account(self):
        return self.__account

    def withdraw(self,amount):
        try:
            if amount>self.__account.get_balance():
                raise OverdrawException
            if amount>self.__account.get_balance():
                raise LimitreachedException
            else:


    def take_card(self):
        print("take your card")

class privillage_customer(customer):
    def __init__(self,customer_id,customer_name,age,account,bonous):
        super().__init__(customer_id,customer_name,age,account)
        self.__bonous=bonous
    def get_bonous(self):
        return self.__bonous
    def withdraw(self,amount):
        pass
    def increase_bonous(self):
        pass
class Account:
    def __init__(self,account_type,balance,min_balance):
        self.__account_type=account_type
        self.__balance=balance
        self.__min_balance=min_balance
    def get_account(self):
        return self.__account_type
    def get_balance(self):
        return self.__balance
    def get_min_balance(self):
        return self.__min_balance
    def set_balance(self,balance):
        self.__balance=balance