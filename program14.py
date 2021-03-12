class Vehicle:
    def __init__(self,vehicle_id,vehicle_type,vehicle_cost):
        self.__vehicle_id=vehicle_id
        self.__vehicle_type=vehicle_type
        self.__vehicle_cost=vehicle_cost
        self.__premium_amount=None
    def set_calculate_premium(self):
        if self.__vehicle_type=="Two wheeler":
            self.__premium_amount=self.__vehicle_cost*2/100
        elif self.__vehicle_type=="Four wheeler":
            self.__premium_amount=self.__vehicle_cost*6/100
        else:
            print("worng vehicle type")
    def get_display_vehicle_deatils(self):
        print("vehicle id :",self.__vehicle_id,
              "vehicle type :",self.__vehicle_type,
              "vehicle cost :",self.__vehicle_cost,
              " vehicle premium :" ,self.__premium_amount)

v1=Vehicle(101,"Two wheeler",60000)
v1.set_calculate_premium()
v1.get_display_vehicle_deatils()

v2 = Vehicle(102,"Four wheeler",500000)
v2.set_calculate_premium()
v2.get_display_vehicle_deatils()