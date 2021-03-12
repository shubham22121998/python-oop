class Customer_information:
    def __init__(self,name,age,acc_type,bank):
        self.__name=name
        self.__age=age
        self.__acc_type=acc_type
        self.bank=bank
    def display(self):
        print(self.__name,self.__age,self.__acc_type,self.bank.get_name(),self.bank.get_acc_no(),self.bank.get_balance())



class Bank:
    def __init__(self,bank_name,acc_no,balance):
        self.__bank_name=bank_name
        self.__acc_no=acc_no
        self.__balance=balance
    def get_name(self):
        return self.__bank_name
    def get_acc_no(self):
        return self.__acc_no
    def get_balance(self):
        return self.__balance

b1=Bank("SBI",1234567,16000)
C1=Customer_information("SHUBHAM",22,"SAVING",b1)
C1.display()