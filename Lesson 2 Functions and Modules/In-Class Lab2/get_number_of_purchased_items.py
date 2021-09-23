def get_number_of_purchased_items():
    """
    Check to make sure that a proper integer unit is entered. If not then keep asking the question and let the user
    know they must enter a proper integer.
    Second Variant, return
    :return: the number of items that the user wants to purchase, in integer format
    """
    while True:
        try:
            number_of_purchased_items = int(input("enter quantity purchased:"))
            return number_of_purchased_items
            # returns the number of items purchased with a integer value
        except ValueError as e:
            print("not a proper integer! Try again")
            # If there is an error then go back to the top of this while loop and try again
