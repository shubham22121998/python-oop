'''
def purchase_list(item,price):
    discount=10
    total_price=price-(price*10/100)
    print("price of ",item,"is",total_price)
purchase_list("mobile",20000)
purchase_list("watch",8000)

'''

def purchase_list(item,price,type=None):
    if item=="mobile":
        if type=="apple":
            discount=10
        else:
            discount=5
        total_price=price-price*discount/100

    else:
        total_price= price + price * 2/100
    print("price of",item,"is",total_price)


purchase_list("mobile",100000,"apple")