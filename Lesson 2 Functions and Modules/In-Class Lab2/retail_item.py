def get_retail_item_description():
    retail_item_description = input("enter retail item description:")
    return retail_item_description


def get_number_of_purchased_items():
    while True:
        try:
            number_of_purchased_items = int(input("enter quantity purchased:"))
            return number_of_purchased_items
        except ValueError as e:
            print("not a proper integer! Try again")


def get_price_per_unit():
    while True:
        try:
            price_per_unit = float(input("enter price per unit:"))
            price_per_unit = "{:.2f}".format(price_per_unit)
            return price_per_unit
        except ValueError as e:
            print("not a proper integer! Try again")


def get_tax_rate():

    while True:
        try:
            tax_rate = float(input("enter tax:"))
            if tax_rate < 1:
                return tax_rate
            else:
                print("Make sure the tax rate has been converted out of percentage format!")
        except ValueError as e:
            print("not a proper integer! Try again")


def calculate_subtotal(price, quantity_sold):
    # calucate subtotal amount. Multiply price of retail item times quantity sold
    subtotal = float(price) * float(quantity_sold)
    subtotal = "{:.2f}".format(subtotal)
    return subtotal


def calculate_tax(subtotal, tax):
    # calculates and returns the tax amount of the given subtotal
    amount_tax = float(subtotal) * float(tax)
    amount_tax = "{:.2f}".format(amount_tax)
    return amount_tax


def calculate_total(subtotal, tax):
    # Takes subtotal and tax. Returns total amount
    amount_total = float(subtotal) + float(tax)
    amount_total = "{:.2f}".format(amount_total)
    return amount_total


def main():
    retail_item_description = get_retail_item_description()
    number_of_purchased_items = get_number_of_purchased_items()
    price_per_unit = get_price_per_unit()
    tax_rate = get_tax_rate()
    calculated_subtotal = calculate_subtotal(price_per_unit, number_of_purchased_items)
    calculated_tax = calculate_tax(calculated_subtotal, tax_rate)
    calculated_total = calculate_total(calculated_subtotal, calculated_tax)
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
