class Flower:
    def __init__(self,flower_name,price_per_kg,stock_avilable):
        self.flower_name=flower_name
        self.price_per_kg=price_per_kg
        self.stock_avilable=stock_avilable

    def validate_flower(self):
        if self.flower_name=="Orchid" or self.flower_name=="Rose" or self.flower_name=="Jasmine":
            return True
        else:
            return False
    def valiadte_stock(self,quantity_required):
        if self.stock_avilable>=quantity_required:
            return True
        else:
            return False
    def sell_flower(self,quantity_required):
        if self.flower_name == "Orchid" or self.flower_name == "Rose" or self.flower_name == "Jasmine":
            if self.stock_avilable >= quantity_required:
               True
            else:
                False
        else:
            False
    def set_updated_record(self,qunatity_sold):
        self.stock_avilable=self.stock_avilable-qunatity_sold
    def get_updated_recoed(self):
        print(self.flower_name,self.stock_avilable,self.price_per_kg)

f1=Flower("Orchid",12,15)
print(f1.validate_flower())
print(f1.valiadte_stock(10))
print(f1.sell_flower(10))
print(f1.set_updated_record(10))
f1.get_updated_recoed()



