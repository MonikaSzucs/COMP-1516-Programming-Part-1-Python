"""
A script to run the calculate_subtotal() function, takes two parameters called price and quantity_sold
and will return the subtotal
:author: Monika Szucs
:date: Sept 26 2021
"""


def calculate_subtotal(price, quantity_sold):
    """
        a function that calculated the subtotal containing the price and quantity sold
        Fifth Variant, parameters and return
        :param price: the price of the purchased item
        :param quantity_sold: the number of items sold
        :return: the subtotal of unit sold, float(price) * float(quantity_sold) and formatted to two decimal places
    """
    subtotal = float(price) * float(quantity_sold)
    subtotal = "{:.2f}".format(subtotal)
    return subtotal
    # return float(price) * float(quantity_sold) and round to two decimal places
