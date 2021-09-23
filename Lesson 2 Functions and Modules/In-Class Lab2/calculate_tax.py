def calculate_tax(subtotal, tax):
    """
    a function to return the amount of tax that should be added to the subtotal amount of units purchased multiplied
    by its price
    Sixth Variant, parameters and return
    :param subtotal:
    :param tax:
    :return:
    """
    # calculates and returns the tax amount of the given subtotal
    amount_tax = float(subtotal) * float(tax)
    amount_tax = "{:.2f}".format(amount_tax)
    return amount_tax