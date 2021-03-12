class InvlaidMachinicIdException(Exception):
    pass
class IvalidMachinicSpecalizationException(Exception):
    pass
class Mechinic:
    def __init__(self,mechinc_id,specialization,vihcle_count):
        self.__mechinc_id=mechinc_id
        self.__specialization=specialization
        self.__vihcle_count=vihcle_count

    def get_mehinc_id(self):
        return self.__mechinc_id

    def get_specialization(self):
        return self.__specialization

    def get_vihcle_count(self):
        return self.__vihcle_count

    def set_mehinc_id(self,mehinc_id):
        self.__mechinc_id=mehinc_id

    def set_specilazion(self,specialization):
        self.__specialization=specialization

    def set_vehicle_count(self,vehicle_count):
        self.__vihcle_count=vehicle_count
class VehicleService(Mechinic):
    def __init__(self,mehinc_list):
        self.__mechic_list=mehinc_list
    def assign_vehicle_for_service(self,mechinc_id,vehicle_type):
        try:
            if self.get_mehinc_id()!=mechinc_id:
                raise InvlaidMachinicIdException
            if self.get_specialization()!=vehicle_type:
                raise IvalidMachinicSpecalizationException
            else:
                 self.set_vehicle_count(1)
        except  InvlaidMachinicIdException:
            print("invalid id")
        except  IvalidMachinicSpecalizationException:
            print("invalid s")
m1=Mechinic(101,"TW",1)
m2=Mechinic(105,"FW",4)

V=VehicleService([m1,m2])
V.assign_vehicle_for_service(104,"TW")




