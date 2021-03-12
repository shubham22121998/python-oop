from abc import ABCMeta,abstractmethod
class product(metaclass=ABCMeta):
    @abstractmethod
    def return_policy(self):
        pass
class mobile(product):
    def return_policy(self):
        print("retuen the the mobile in 10 days if you have any problem")

class feature_phone(mobile):
    pass

class smart_phone(mobile):
    pass
mobile().return_policy()



