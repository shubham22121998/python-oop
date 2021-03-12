#OOPR-Exer-8
class Juggler:
    def __init__(self,name,jugglingitem):
        self.__name=name
        self.jugglingitem=jugglingitem

    def juggles(self):
        print(self.__name,"is juggling with",self.jugglingitem.get_name())

class JugglingItem:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name

ji1=JugglingItem("knife")
ji2=JugglingItem("Ball")

j1=Juggler("Jack Bremlov",ji1)
j2=Juggler("Anthony Gatto",ji2)
j1.juggles()
j2.juggles()