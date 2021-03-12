class shoes:
    def __init__(self,brand,material):
        self.brand=brand
        self.material=material
    def __str__(self):
        return "name of brand is" + str(self.brand) + "materi8als name" + self.material
s1=shoes(10000,"leather")
print(s1)