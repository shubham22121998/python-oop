class Ticket:
    counter=00
    def __init__(self,passenger_name,source,destination):
        self.passenger_name=passenger_name
        self.source=source
        self.destination=destination
        self.ticket_id=None
        Ticket.counter+=1

    def validate_source_destination(self):
        if self.source=="Delhi" and(self.destination=="Pune" or self.destination=="Mumbai" or self.destination=="Chennai" or self.destination=="Kolkata"):
                return True
        else:
            False
    def genrate_ticket(self):
        if self.validate_source_destination()==True:

            srcchar=self.source[0].upper()
            deschar=self.destination[0].upper()

            if (Ticket.counter<10):
                self.ticket_id= srcchar + deschar+"0"+str(Ticket.counter)
            else:
                self.ticket_id= srcchar + deschar+str(Ticket.counter)
        else:
            self.ticket_id =None
            return self.ticket_id


    def get_ticket_id(self):
        return self.ticket_id
    def get_passenger_name(self):
        return self.passenger_name
    def get_source(self):
        if self.source=="Delhi":
            return self.source
        else:
            print("you have written invalid soure option")
            return None
    def get_destination(self):
        if self.destination=="Pune":
            return self.destination
        elif self.destination=="Mumbai":
            return self.destination
        elif self.destination=="Chennai":
            return self.__destination
        elif self.destination=="Kolkata":
            return self.destination

        else:
            return None
    def get_ticket_print(self):
        print(self.passenger_name,self.source,self.destination,self.ticket_id)

t1=Ticket("SHUBHAM","Delhi","Mumbai")
print(t1.validate_source_destination())
print(t1.genrate_ticket())
print(t1.get_ticket_id())
print(t1.get_source())
print(t1.get_destination())
t1.get_ticket_print()

