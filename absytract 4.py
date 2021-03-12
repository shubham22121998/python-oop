from abc import ABCMeta , abstractmethod
class parent(metaclass=ABCMeta):
    def __init__(self):
        self.val=5
    @abstractmethod
    def show(self):
        pass
class child(parent):
    def __init__(self):
        super().__init__()
        self.num=100
class grand_child(child):
    def show(self):
        print(self.num)
        print(self.val)
        print("this is possible")
g=grand_child()
g.show()
