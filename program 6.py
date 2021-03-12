class example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
obj1=example(10)
print(obj1.get_num())

obj1.set_num(15)
print(obj1.get_num())

'''
class num:
    def __init__(self,cust_id):
        cust_id=100
c1=num(200)
print(c1.cust_id) # error


class num2:
    def __init__(self):
        cust_id=100
c1=num2(200)
print(c1.cust_id) #error

'''
class num3:
    def __init__(self,num):
        self.num=num

c1=num3(200)
print(c1.num)



