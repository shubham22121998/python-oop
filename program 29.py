class Lion:
    __water_source="well in the zoo"
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def drink_water(self):
        print(self.name ,"drink water from",Lion.__water_source)
    @staticmethod
    def get_water_source():
        return Lion.__water_source
l1=Lion("simba","Male")
l1.drink_water()

print("lion get water from",Lion.get_water_source())