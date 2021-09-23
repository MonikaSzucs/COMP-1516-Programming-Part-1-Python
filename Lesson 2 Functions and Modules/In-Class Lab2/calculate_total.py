def calculate_total(subtotal, tax):
    """
    a function to return the total amount that the person needs to pay based on the number of units bought,
    the price, and tax needed to pay
    Eighth variant, paramters, and return
    :param subtotal: the sub total consists of the number of units bought multiplied by the price per unit
    :param tax: the amount of tax that must be paid based on the subtotal
    :return: the total amount that must be paid
    """
    amount_total = float(subtotal) + float(tax)
    amount_total = "{:.2f}".format(amount_total)
    return amount_total
    # return the total amount that must be paid
