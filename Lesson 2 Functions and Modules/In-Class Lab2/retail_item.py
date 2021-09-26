"""
A script with the main function used to call all the other functions
:author: Monika Szucs
:date: Sept 26 2021
"""


import get_retail_item_description
import get_number_of_purchased_items
import get_price_per_unit
import get_tax_rate
import calculate_subtotal
import calculate_tax
import calculate_total


def main():
    retail_item_description = get_retail_item_description.get_retail_item_description()
    number_of_purchased_items = get_number_of_purchased_items.get_number_of_purchased_items()
    price_per_unit = get_price_per_unit.get_price_per_unit()
    tax_rate = get_tax_rate.get_tax_rate()
    calculated_subtotal = calculate_subtotal.calculate_subtotal(price_per_unit, number_of_purchased_items)
    calculated_tax = calculate_tax.calculate_tax(calculated_subtotal, tax_rate)
    calculated_total = calculate_total.calculate_total(calculated_subtotal, calculated_tax)
    print("Sales Receipt:")
    print("Item Description: ", retail_item_description)
    print("Number of Purchased items: ", number_of_purchased_items)
    print("Unit Price: ", price_per_unit)
    print("Tax Rate: ", tax_rate)
    print("Subtotal: ", calculated_subtotal)
    print("Tax: ", calculated_tax)
    print("Total: ", calculated_total)


if __name__ == "__main__":
    main()
