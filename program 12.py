class Table:
    def __init__(self):
        no_of_legs=4
        self.__glasstop=None
        self.__woodentop=None
    def assign_glass(self,glasstop,woodentop):
        self.__glasstop=glasstop
        self.__woodentop=woodentop
    def identiyfy_rate(self,glasstop,woodentop):
        self.assign_glass(glasstop,woodentop)
        if self.__glasstop==True:
            rate=30000
        elif self.__woodentop==True:
            rate=20000
        else:
            rate=0
        return rate
difining_rate=Table()
rate=difining_rate.identiyfy_rate(True,False)
print(rate)

