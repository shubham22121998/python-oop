class University:
    def __init__(self,student_id,marks,age):
        self.__student_id=student_id
        self.__marks=marks
        self.__age=age
        self.__course_id=None
        self.__fees=None
    def set_validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    def set_vailadate_marks(self):
        if self.__marks>0 and self.__marks<100:
            return True
        else:
            return False
    def set_chek_qualification(self):
        if self.__age>20:
            if self.__marks>=65:
                return True
            else:
                return False
        else:
            return False
    def set_fees_structure(self,course_id):
        if course_id==1001 or course_id==1002:


    def get_all_details(self):
        return print(self.__student_id,self.__marks,self.__age)
s1 = University(101,0,21)
print(s1.set_validate_age())
print(s1.set_vailadate_marks())
print(s1.set_chek_qualification())
s1.get_all_details()
