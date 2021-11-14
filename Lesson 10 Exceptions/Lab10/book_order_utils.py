"""
Lab 10 by Monika Szucs A00878763
A script containing the main() function
:author: Monika Szucs
:date: November 15, 2021
"""

import re


def validate_book_order_details(order_num, title, author, isbn, year, quantity, cost):
    try:
        print(order_num)
        print(int(order_num))
        order_num_array = [order_num]
        removed_leading_zeros = [ele.lstrip('0') for ele in order_num_array]
        print(str(removed_leading_zeros))
        print(len(removed_leading_zeros[0]))
        print(order_num_array)
        print("--Order Number-")
        leading_zeros_amount = 0
        while True:
            if len(removed_leading_zeros[0]) == leading_zeros_amount:
                break
            else:
                leading_zeros_amount += 1
        print(leading_zeros_amount)
    except ValueError:
        print("Order Number is invalid")
    try:
        print("--Title--")
        if re.search("^[a-zA-Z\s]+$", title):
            print(title)
        else:
            print("Title is invalid")
    except (ValueError, TypeError):
        print("Title is invalid")
    try:
        print("--author--")
        if re.search("^[a-zA-Z\s\'\"]+$", author):
            print(author)
        else:
            print("Author is invalid")
    except (ValueError, TypeError):
        print("Author is invalid.")
    try:
        print("--ISBN--")
        if re.search("^[0-9]{4,20}$", isbn):
            print(isbn)
        else:
            print("ISBN must be an integer")
    except (ValueError, TypeError):
        print("ISBN must be an integer.")
    try:
        print("--Year--")
        print(int(year))
        if re.search("^[0-9]{4}$", year):
            print(year)
        else:
            print("Year is invalid")
    except (ValueError, TypeError):
        print("Year must be an integer.")
    try:
        print("--Quantity--")
        print(int(quantity))
        if re.search("^[0-9]{0,1000}$", quantity):
            print(quantity)
        else:
            print("Quantity is invalid")
    except (ValueError, TypeError):
        print("Quantity must be an integer.")
    try:
        print("--Cost--")
        print(cost)
        print(float(cost))
        if re.search("^\d+\.\d{2}$", cost):
            print(cost)
        else:
            print("Cost is invalid")
    except (ValueError, TypeError):
        print("Cost is invalid.")
    print()


def calculate_per_book_cost(cost, quantity):
    print(cost)
    print(quantity)
    try:
        cost_per_book = cost/quantity
        print(cost_per_book)
        return cost_per_book
    except ZeroDivisionError:
        return "The quantity cannot be zero"
    print()


def write_book_order_details(filename, title, author, isbn, year, quantity, cost, unit_cost):
    while True:
        try:
            f = open(filename, "x")
            print(filename)
            f.write("Now the file has more content!")
            f.close()
            print(title)
            print(author)
            print(isbn)
            print(year)
            print(quantity)
            print(cost)
            print(unit_cost)
            break
        except FileExistsError:
            filename = input("Please enter another file name because it has already been used: ")

