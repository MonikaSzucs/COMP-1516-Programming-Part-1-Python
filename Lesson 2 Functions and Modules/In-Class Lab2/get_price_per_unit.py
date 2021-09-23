def get_price_per_unit():
    while True:
        try:
            price_per_unit = float(input("enter price per unit:"))
            price_per_unit = "{:.2f}".format(price_per_unit)
            return price_per_unit
        except ValueError as e:
            print("not a proper integer! Try again")