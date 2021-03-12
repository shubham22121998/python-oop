class Parent:
    def __init__(self):
        self.__num=100
    def show(self):
        print(self.__num)
class child(Parent):
    def __init__(self):
        super().__init__()
        self.__val=200
    def show(self):
        super().show()
        print(self.__val)
son=child()
son.show()
