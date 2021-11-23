"""
Lab 10 by Monika Szucs A00878763
A script containing the main() function in main.py
:author: Monika Szucs
:date: November 22, 2021
"""

from book_order_utils import validate_book_order_details, calculate_per_book_cost, write_book_order_details


def main():
    order_num = input("Enter a order number: ")
    title = input("Enter a title: ")
    author = input("Enter a author: ")
    isbn = input("Enter a isbn: ")
    year = input("Enter a year: ")
    quantity = input("Enter a quantity: ")
    cost = input("Enter a cost: ")
    unit_cost = input("Enter a unit_cost: ")
    validate_book_order_details(order_num, title, author, isbn, year, quantity, cost)
    print()
    print(calculate_per_book_cost(12.00, 2))
    print()
    print(calculate_per_book_cost(12.00, 0))
    print()
    filename = input("Please enter a file name: ")
    write_book_order_details(filename, title, author, isbn, year, quantity, cost, unit_cost)


if __name__ == "__main__":
    main()
