class Credit_Card:
    def __init__(self,card_no,balance):
        self.card_no=card_no
        self.balance=balance
class Customer:
    def __init__(self,card):
        self.card=card

    def purchase_item(self,price,card_no):
        if price<0:
            raise Exception("Invalid price")
        if card_no not in self.card:
            raise Exception("wrong card")
        if price>self.card[card_no].balance:
            raise Exception("invalid c")
card1=Credit_Card(101,800)
card2=Credit_Card(102,1000)
card3=Credit_Card(103,1100)
card_dic={card1.card_no:card1,card2.card_no:card2,card3.card_no:card3}
c=Customer(card_dic)

while (True):
    card_no=int(input("enter your card no"))
    try:
        c.purchase_item(1200,101)
        break
    except Exception as e:
        if str(e)=="invalid price":
            print(" product is wrong")
            break
        if str(e)=="wrong card":
            continue


