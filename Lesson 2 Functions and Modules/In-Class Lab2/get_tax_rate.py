def get_tax_rate():
    """
    a function that will return the tax rate that is less than the value of 1 and is a float
    Fourth Variant, parameters, and return
    :param tax_rate: the rate of the tax that is entered from the use that is less than the value of 1
    :return: the tax rate that is less than 1
    """
    while True:
        try:
            tax_rate = float(input("enter tax:"))
            if tax_rate < 1:
                return tax_rate
            else:
                print("Make sure the tax rate has been converted out of percentage format!")
            # this is a if statement to check if the tax rate entered is less than 1
            # if not then let the user know it must be a value less than 1
        except ValueError as e:
            print("not a proper integer! Try again")
            # if the wrong value type is entered in then run this error prompt and start from the top of the while loop
