import re


def validate_book_order_details(order_num, title, author, isbn, year, quantity, cost):
    print(order_num)
    print(int(order_num))
    order_num_array = []
    order_num_array.append(order_num)
    removed_leading_zeros = [ele.lstrip('0') for ele in order_num_array]
    print(str(removed_leading_zeros))
    print(len(removed_leading_zeros[0]))
    print("---")
    leading_zeros_amount = 0
    while True:
        if len(removed_leading_zeros[0]) == leading_zeros_amount:
            print("equals")
            break
        else:
            leading_zeros_amount += 1
    print("done")
    print(leading_zeros_amount)
    print("---")


def calculate_per_book_cost(cost, quantity):
    pass


def write_book_order_details(filename, title, author, isbn, year, quantity, cost, unit_cost):
    pass
