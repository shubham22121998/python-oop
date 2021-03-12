from abc import ABCMeta,abstractmethod
class Product(metaclass=ABCMeta):
    @abstractmethod
    def return_policy(self):
        pass
class mobile(Product):
    pass
#mobile()
# ifwe3 declear the parent class as abstract class then the sub class has override the abstract method if we
# do not do that we can an error
#TypeError: Can't instantiate abstract class mobile with abstract method return_policy

class phone(metaclass=ABCMeta):
    @abstractmethod
    def return_ploicy(self):
        pass
class Mobile(phone):
    def return_ploicy(self):
        print("retuen the phone in 10 days if you have any problem ih th phone")
Mobile().return_ploicy()