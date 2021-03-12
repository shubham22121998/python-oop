class parent:
    def __init__(self,num):
        self.__num=num
    def get_num(self):
        return self.__num
class child(parent):
    def __init__(self,val,num):
        self.__val=val

    def get_val(self):
        return self.__val
son=child(100,10)
print(son.get_num())
print(son.get_val())

'''
 return self.__num
AttributeError: 'child' object has no attribute '_parent__num'
'''