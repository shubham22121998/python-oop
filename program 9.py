class Employee:
    def __init__(self,dep,sal):
        self.dep=dep
        self.sal=sal
        self.new_salary=None
    def salary_count(self):
        if self.dep=="IT":
            increment=5
        elif self.dep=="hr":
            increment=3
        else:
            increment=1
        self.new_salary=self.sal+self.sal * increment/100
        print("you  current salry  is :",self.sal,"and icrement salary :",self.new_salary)


s1=Employee("IT",40000)
s2=Employee("hr",56000)
s3=Employee("sale",3000)

s1.salary_count()
s2.salary_count()
s3.salary_count()
