def calculate_subtotal(price, quantity_sold):
    """
        a function that calculated the subtotal containing the price and quantity sold
        Fifth Variant, parameters and return
        :param price: the price of the purchased item
        :param quantity_sold: the number of items sold
        :return: the subtotal of unit sold, float(price) * float(quantity_sold) and formatting it to two decimal places
    """
    # calucate subtotal amount. Multiply price of retail item times quantity sold
    subtotal = float(price) * float(quantity_sold)
    subtotal = "{:.2f}".format(subtotal)
    return subtotal
    # return float(price) * float(quantity_sold) and round to two decimal places
