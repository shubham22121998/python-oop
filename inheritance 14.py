class Bick_ride:
    def __init__(self,race_licence):
        self.__race_licence=race_licence
        self.__trained_status=None
        self.__experince=None
    def ride_on_dome(self):
        if (self.__race_licence==True) and (self.__trained_status==True) and (self.__experince>=5):
            print("ride the bick")
        else:
            print("not ride the bick")
    def get_licence(self):
        return self.__race_licence
    def get_trained(self):
        return self.__trained_status
    def get_experince(self):
        return self.__experince
class cycle_ride:
    def ride_lindfold(self):
        pass


class Ride:
    def __init__(self,trained_status,experince):
        self.__trained_status=trained_status
        self.__experince=experince
    def ride_vichel(self):
        if self.__trained_status.get_trained() and self.__experince.get_experince():
            print("ride the vihcle")
        else :
            print("not ride the vihcle")