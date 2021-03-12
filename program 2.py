def purchase_list(product,brand,price,materials):
    if product=="mobile":
        if brand=="apple":
            discount=10
        else:
            discount=5
        total_price=price-price*discount/100
    else:
        if materials=="lather":
            tax=5
        else:
            tax=2
        total_price=price+price*tax/100
    print("product type is",product,"price is",total_price)
purchase_list("shoe",None,20000,"lather")
