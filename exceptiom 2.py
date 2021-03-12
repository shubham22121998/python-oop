class NmaeLengthException(Exception):
    pass
class EmployeeIdException(Exception):
    pass
class Employee:
    __trails=0
    def __init__(self,employee_id,employee_name):
        self.__employee_name=employee_name
        self.__employee_id=employee_id
    def validate_name(self):
        try:
            if (len(self.__employee_name) < 4):
                Employee.__trails = Employee.__trails + 1
                raise NmaeLengthException
            if (not (self.__employee_id.startswith("E"))):
                Employee.__trails = Employee.__trails + 1
                raise EmployeeIdException
        except NmaeLengthException:
            Employee.__trails=Employee.__trails+1
            print(Employee.__trails)
        except EmployeeIdException:
            Employee.__trails=Employee.__trails+1
            print(Employee.__trails)
E1=Employee("E1001","TOM")
E1.validate_name()
E2=Employee("1001","SHUBHAM")
E2.validate_name()

