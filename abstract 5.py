from abc import ABCMeta,abstractmethod
class DirectToHomeService(metaclass=ABCMeta):
    counter=101
    def __init__(self,consumer_name):
        self.__consumer_name=consumer_name
        self.__consumer_id=DirectToHomeService.counter
        DirectToHomeService.counter+1
    def get_consumer_name(self):
        return self.__consumer_name
    def get_consumer_id(self):
        return self.__consumer_id
    @abstractmethod
    def calaculate_monthly_rate(self):
        pass
class Basepakageclass(DirectToHomeService):
    def __init__(self,consumer_name,base_pack_name,sub_period):
        super().__init__(consumer_name)
        self.__base_pack_name=base_pack_name
        self.__sub_period=sub_period
    def get_base_pack_name(self):
        return self.__base_pack_name
    def get_sun_period(self):
        return self.__sub_period
    def valid_base_pack_name(self):
        if self.get_base_pack_name()==("Silver").upper() or self.get_base_pack_name()==("Gold").upper() or self.get_base_pack_name()==("Platinum").upper():
            return True
        else:
            self.__base_pack_name="Silver"
            print("base pack name is invalid set to silver")
            return  True
    def calaculate_monthly_rate(self):
        if self.__sub_period>=1 and self.__sub_period<=24:
            if self.valid_base_pack_name() is True:
                if self.__sub_period>12:
                    if self.__base_pack_name=="Silver":
                        discount=350.0
                        monthly_rent=350.0
                    elif self.__base_pack_name=="Gold":
                        discount=440.0
                        monthly_rent=440.0
                    elif self.__base_pack_name=="Platinum":
                        discount=560.0
                        monthly_rent=560.0
                else:
                    if self.__base_pack_name=="Silver":
                        discount=0
                        monthly_rent=350.0
                    elif self.__base_pack_name=="Gold":
                        discount=0
                        monthly_rent=440.0
                    elif self.__base_pack_name=="Platinum":
                        discount=0
                        monthly_rent=560.0
                final_monthly_rent=((monthly_rent*self.__sub_period)-discount)/self.__sub_period
                return final_monthly_rent
            else:
                return -1
        else:
            return -1

obj1=Basepakageclass("SHUBHAM","Gold",23)
res=obj1.calaculate_monthly_rate()
print(res)