#how to import abstract method
from abc import ABCMeta ,abstractmethod
class Product(metaclass=ABCMeta):
    @abstractmethod
    def return_policy(self):
        print("product can be retuned")


#how can we make the erroe in this method
class phone(metaclass=ABCMeta):
    @abstractmethod
    def return_policy(self):
        pass

phone()
# if we instantiated the abstract method class then we goth an error
#TypeError: Can't instantiate abstract class phone with abstract method return_policy