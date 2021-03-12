from  abc import ABCMeta , abstractmethod

class Employee(metaclass=ABCMeta):
    def __init__(self,job_band,employee_name,basic_salary,qualification):
        self.__job_band=job_band
        self.__employee_name=employee_name
        self.__basic_salary=basic_salary
        self.__qualification=qualification

    def get_job_band(self):
        return self.__job_band
    def get_employee_name(self):
        return self.__employee_name
    def get_basic_salary(self):
        return self.__basic_salary
    def get_basic_qualification(self):
        return self.__qualification

    def validate_basic_salary(self):
        if self.__basic_salary>=3000:
            return True
        return False
    def validate_qualification(self):
        if self.__qualification=="Bechlore" or self.__qualification=="Master":
            return True
        return False
    @abstractmethod
    def validate_job_band(self):
        pass
    @abstractmethod
    def calacualte_gross_salary(self):
        pass


class Graduate(Employee):
    def __init__(self,job_band,employee_name,basic_salary,qualification,cgpa):
        super().__init__(job_band,employee_name,basic_salary,qualification)
        self.__cgpa=cgpa
    def get_cgpa(self):
        return self.__cgpa

    def validate_job_band(self):
        if self.get_job_band()=="A" or self.get_job_band()=="B" or self.get_job_band()=="C":
            return True
        return False

    def calacualte_gross_salary(self):
        if (self.validate_basic_salary() is True) and (self.validate_qualification() is True) and (self.validate_job_band() is True):
            if (self.get_job_band()=="A"):
                if (self.__cgpa>=4 and self.__cgpa<=4.25):
                    gross_salary  =self.get_basic_salary() +(self.get_basic_salary() *12/100)+1000+(self.get_basic_salary() * 4/100)
                elif  (self.__cgpa>=4.26 and self.__cgpa<=4.5):
                    gross_salary = self.get_basic_salary() + (self.get_basic_salary() * 12/100) + 1700 +(self.get_basic_salary() * 4/100)
                elif (self.__cgpa >= 4.51 and self.__cgpa <= 4.75):
                    gross_salary = self.get_basic_salary() + (self.get_basic_salary() * 12 / 100) + 3200 + (self.get_basic_salary() * 4 / 100)

                elif (self.__cgpa >= 4.76 and self.__cgpa <= 5):
                    gross_salary = self.get_basic_salary() + (self.get_basic_salary() * 12 / 100) + 5000 + (self.get_basic_salary() * 4 / 100)
                else:
                    gross_salary=-1
                    return gross_salary
            elif (self.get_job_band()=="B"):
                if (self.__cgpa >= 4 and self.__cgpa <= 4.25):
                    gross_salary = self.get_basic_salary() + (self.get_basic_salary() * 12 / 100) + 1000 + (
                                self.get_basic_salary() * 6 / 100)
                elif (self.__cgpa >= 4.26 and self.__cgpa <= 4.5):
                    gross_salary = self.get_basic_salary() + (self.get_basic_salary() * 12 / 100) + 1700 + (
                                self.get_basic_salary() * 6 / 100)
                elif (self.__cgpa >= 4.51 and self.__cgpa <= 4.75):
                    gross_salary = self.get_basic_salary() + (self.get_basic_salary() * 12 / 100) + 3200 + (
                                self.get_basic_salary() * 6 / 100)

                elif (self.__cgpa >= 4.76 and self.__cgpa <= 5):
                    gross_salary = self.get_basic_salary() + (self.get_basic_salary() * 12 / 100) + 5000 + (
                                self.get_basic_salary() * 6 / 100)
                else:
                    gross_salary = -1
                    return gross_salary
            elif (self.get_basic_salary()=="C"):
                if (self.__cgpa>=4 and self.__cgpa<=4.25):
                    gross_salary  =self.get_basic_salary() +(self.get_basic_salary() *12/100)+1000+(self.get_basic_salary() * 10/100)
                elif  (self.__cgpa>=4.26 and self.__cgpa<=4.5):
                    gross_salary = self.get_basic_salary() + (self.get_basic_salary() * 12/100) + 1700 +(self.get_basic_salary() * 10/100)
                elif (self.__cgpa >= 4.51 and self.__cgpa <= 4.75):
                    gross_salary = self.get_basic_salary() + (self.get_basic_salary() * 12 / 100) + 3200 + (self.get_basic_salary() * 10 / 100)

                elif (self.__cgpa >= 4.76 and self.__cgpa <= 5):
                    gross_salary = self.get_basic_salary() + (self.get_basic_salary() * 12 / 100) + 5000 + (self.get_basic_salary() * 10 / 100)
                else:
                    gross_salary=-1
                    return gross_salary
            else:
                gross_salary=-1
                return gross_salary
            return print("gradute employee slary after the all thigs add up",gross_salary)
        else:
            return -1

class  Lateral(Employee):
    def __init__(self,job_band,employee_name,basic_salary,qualification,skill_set):
        super().__init__(job_band,employee_name,basic_salary,qualification)
        self.__skill_set=skill_set
    def get_skill_set(self):
        return self.__skill_set
    def validate_job_band(self):
        if self.get_job_band()=="D" or self.get_job_band()=="E" or self.get_job_band()=="F":
            return True
        return False
    def calacualte_gross_salary(self):
        gross_salary=0
        if (self.validate_qualification() is True) and  (self.validate_qualification() is True) and (self.validate_basic_salary()):
            if self.__skill_set=="AGP":
                if self.get_job_band()=="D":
                    gross_salary=self.get_basic_salary() +(self.get_basic_salary() *12/100)+6500+(self.get_basic_salary()*13/100)
                elif self.get_job_band()=="E":
                    gross_salary=self.get_basic_salary() +(self.get_basic_salary() *12/100)+6500+(self.get_basic_salary()*16/100)
                elif self.get_job_band()=="F":
                    gross_salary = self.get_basic_salary() + (self.get_basic_salary() * 12 / 100)  + 6500 + (
                                self.get_basic_salary() * 20 / 100)
                else:
                    gross_salary=-1
                    return gross_salary
            elif self.__skill_set=="AGPT":
                bonous=8200
                if self.get_job_band() == "D":
                    gross_salary = self.get_basic_salary() + (self.get_basic_salary() * 12 / 100) + bonous + (
                                self.get_basic_salary() * 13 / 100)
                elif self.get_job_band() == "E":
                    gross_salary = self.get_basic_salary() + (self.get_basic_salary() * 12 / 100) + 1000 + bonous + (
                                self.get_basic_salary() * 16 / 100)
                elif self.get_job_band() == "F":
                    gross_salary = self.get_basic_salary() + (self.get_basic_salary() * 12 / 100) + 1000 + bonous + (
                            self.get_basic_salary() * 20 / 100)
                else:
                    gross_salary = -1
                    return gross_salary
            elif self.__skill_set=="AGDEV":
                bonous=11500
                if self.get_job_band() == "D":
                    gross_salary = self.get_basic_salary() + (self.get_basic_salary() * 12 / 100) + bonous + (
                                self.get_basic_salary() * 13 / 100)
                elif self.get_job_band() == "E":
                    gross_salary = self.get_basic_salary() + (self.get_basic_salary() * 12 / 100)  + bonous + (
                                self.get_basic_salary() * 16 / 100)
                elif self.get_job_band() == "F":
                    gross_salary = self.get_basic_salary() + (self.get_basic_salary() * 12 / 100)  + bonous + (
                            self.get_basic_salary() * 20 / 100)
                else:
                    gross_salary = -1
                    return gross_salary
            else:
                gross_salary=-1
                return gross_salary
            return print("salary of the employee afte the all thigs add up",gross_salary)
        else:
            return -1


s = Graduate("A","SHUBHAM",5000,"Bechlore",4.3)
s.calacualte_gross_salary()

l = Lateral("D","SHUBHAM",150000,"Master","AGDEV")
l.calacualte_gross_salary()


s1 = Graduate("B","atul",10000,"Bechlore",4.75)
s1.calacualte_gross_salary()

l1=Lateral("E","SHUBHAM",90000,"Master","AGP")
l1.calacualte_gross_salary()