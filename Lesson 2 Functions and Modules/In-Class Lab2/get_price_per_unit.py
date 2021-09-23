def get_price_per_unit():
    """
    a function that will return the price of one unit that is a float and contains two decimal places
    Third Variant, parameters, return
    :return: the price of once unit which is a float containing two decimal places, dollar units
    """
    while True:
        try:
            price_per_unit = float(input("enter price per unit:"))
            price_per_unit = "{:.2f}".format(price_per_unit)
            return price_per_unit
            # returning the price of one unit in a float with two decimal places
        except ValueError as e:
            print("not a proper integer! Try again")
            # Will show an error and tell the user to enter in another number and try again