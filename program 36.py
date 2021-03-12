class Parrot:
    counter=7001
    def __init__(self,name,color):
        self.__name=name
        self.__color=color
        self.__unique_number=Parrot.counter
        Parrot.counter+=1
    def display(self):
        print(self.__name,self.__color,self.__unique_number)
    def get_name(self):
        return self.__name
    def get_color(self):
        return self.__color
p1 = Parrot("shubham","grenn")
p1.display()
p2=Parrot("atul","yellow")
p2.display()
p3=Parrot("jaki","red")
p3.display()