class Customer:
    def __init__(self,customer_name,quantity):
        self.__customer=customer_name
        self.__quantity=quantity

    def  get_customer_name(self):
        return self.__customer
    def get_quantity(self):
        return self.__quantity

    def validate_quantity(self):
        if self.__quantity>=1 and self.__quantity<=5:
            return True
        return False
class PizzaService(Customer):
    __counter=100
    def __init__(self,customer,quantity,pizza_type,additional_tooping):
        super().__init__(customer,quantity)
        PizzaService.__counter+=1
        self.__servide_id=pizza_type[0] + str(PizzaService.__counter)
        self.pizza_cost=None
        self.__pizza_type = pizza_type
        self.__customer=customer
        self.__additional_tooping=additional_tooping


    def get_servide_id(self):
        return self.__servide_id

    def get_customer(self):
        return self.__customer

    def get_additional_tooping(self):
        return self.__additional_tooping

    def get_pizza_type(self):
        return self.__pizza_type

    def validate_pizz_type(self):
        if self.__pizza_type=="Small" or self.__pizza_type=="Medium":
            return True
        return False
    def calculate_pizza_cost(self):
        if self.validate_pizz_type() is True:
            small=150
            medium=200

            if (self.__pizza_type=="Small") and (self.__additional_tooping==True):
                self.pizza_cost=self.validate_quantity()*(small +  35)
            elif (self.__pizza_type=="Small") and (self.__additional_tooping==False):
                self.pizza_cost=small * self.validate_quantity()
            elif (self.__pizza_type=="Medium") and (self.__additional_tooping==True):
                self.pizza_cost=(medium + 50) * self.validate_quantity()
            elif (self.__pizza_type=="Medium") and (self.__additional_tooping==False):
                self.pizza_cost=medium * self.validate_quantity()
            else:
                self.pizza_cost=-1
                return self.pizza_cost

            return self.pizza_cost
        else:
            print("enter wrong type of pizza")

    def  show(self):
        print("Tookn no of customer",self.get_servide_id(),
              "name of the customer",self.get_customer_name(),
               "pizza type",self.get_pizza_type(),
               "piza price",self.pizza_cost)


class Dorrdilivery(PizzaService):
    def __init__(self,customer,quantity,pizza_type,additional_tooping,distance_in_km):
        super().__init__(customer,quantity,pizza_type,additional_tooping)
        self.__distance_in_km=distance_in_km
        self.__dilivery_charge=None

    def get_distance_in_km(self):
        return self.__distance_in_km

    def get_dilivery_charger(self):
        return self.__dilivery_charge



    def validate_distance(self):
        if self.__distance_in_km>=1 and self.__distance_in_km<=10:
            return True
        return False

    def calculate_pizza_cost(self):
        if self.__distance_in_km is True:
            if self.__distance_in_km<=5:
                self.pizza_cost=super().calculate_pizza_cost()+(self.__distance_in_km*5)+self.validate_quantity()
            elif self.__distance_in_km>5:
                self.pizza_cost=super().calculate_pizza_cost()+(self.__distance_in_km*7)+self.validate_quantity()
            else:
                self.pizza_cost=-1
                return self.pizza_cost
            return self.pizza_cost
    def  show(self):
        print("Tookn no of customer",self.get_servide_id(),
              "name of the customer",self.get_customer(),
               "pizza type",self.get_pizza_type(),
               "piza price",self.pizza_cost)

p=PizzaService("shubham",3,"Small",True)
p.calculate_pizza_cost()
p.show()

d =Dorrdilivery("shubham",4,"Medium",True,4)
d.calculate_pizza_cost()
d.show()





