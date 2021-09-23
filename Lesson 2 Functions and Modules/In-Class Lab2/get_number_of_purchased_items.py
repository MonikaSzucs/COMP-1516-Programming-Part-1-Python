def get_number_of_purchased_items():
    while True:
        try:
            number_of_purchased_items = int(input("enter quantity purchased:"))
            return number_of_purchased_items
        except ValueError as e:
            print("not a proper integer! Try again")