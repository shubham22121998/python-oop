class Item:
    def __init__(self,item_id,description,price_per_quantity):
        self.__item_id=item_id
        self.__description=description
        self.__price_per_quantity=price_per_quantity
    def get_item_id(self):
        return self.__item_id
    def get_description(self):
        return self.__description
    def get_price_per_quantity(self):
        return self.__price_per_quantity


class customer:

    def __init__(self,customer_name):
        self.__customer_name=customer_name
        self.__payment_status=None

    def pay_bill(self,bill):
        pass
    def get_customer_name(self):
        return self.__customer_name
    def get_payment_status(self):
        return self.__payment_status
class Bill:
    counter=1001
    def __init__(self,bill_id,bill_amount):
        self.__bill_id=bill_id
        self.__bill_amount=bill_amount
        Bill.counter+1
    def genrate_bill_id(self):
        self.__bill_id="B"+str(Bill.counter)

    def genrate_bill_amount(self,item_quantity,items):
        self.__bill_amount= item_quantity*self.get_price_per_quantity

    def get_bill_id(self):
        return self.__bill_id
    def get_bill_amount(self):
        return self.__bill_amount

