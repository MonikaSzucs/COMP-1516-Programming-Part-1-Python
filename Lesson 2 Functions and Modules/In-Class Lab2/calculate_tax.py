def calculate_tax(subtotal, tax):
    """
    a function to return the amount of tax that should be added to the subtotal amount of units purchased multiplied
    by its price
    Sixth Variant, parameters and return
    :param subtotal: the total calculated by multiplying the amount of units bought by the number of units
    :param tax: the tax amount at a given location, in decimal places under the value of 1.00 with two decimal places
    :return: the amount of tax that must be paid, returned with the value of two decimal places and less than 1.00
    """
    amount_tax = float(subtotal) * float(tax)
    amount_tax = "{:.2f}".format(amount_tax)
    return amount_tax
    # return the amount of tax caluclated from float(subtotal) * float(tax)