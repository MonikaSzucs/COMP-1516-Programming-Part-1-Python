"""
Lab 10 by Monika Szucs A00878763
A script containing the main() function
:author: Monika Szucs
:date: November 15, 2021
"""

import re


def validate_book_order_details(order_num, title, author, isbn, year, quantity, cost):
    try:
        print("--Order Number-")
        order_num_converted = int(order_num)
        if type(order_num_converted) == int:
            order_num_array = [order_num]
            removed_leading_zeros = [ele.lstrip('0') for ele in order_num_array]
            leading_zeros_amount = 0
            while True:
                if len(removed_leading_zeros[0]) == leading_zeros_amount:
                    break
                else:
                    leading_zeros_amount += 1
            print(leading_zeros_amount)
            print("--Title--")
            if re.search("^[a-zA-Z\s]+$", title):
                print(title)
                print("--author--")
                if re.search("^[a-zA-Z\s\'\"]+$", author):
                    print(author)
                    print("--ISBN--")
                    if re.search("^[0-9]{4,20}$", isbn):
                        print(isbn)
                        print("--Year--")
                        if re.search("^[0-9]{4}$", year):
                            print(year)
                            print("--Quantity--")
                            if re.search("^([0-9]|[1-9][0-9]|[1-9][0-9][0-9]|1000)$", quantity):
                                print(quantity)
                                print("--Cost--")
                                if re.search("^\d+\.\d{2}$", cost):
                                    print(cost)
                                else:
                                    raise ValueError("cost must be a floating point value with exactly 2 decimal places")
                            else:
                                if (len(quantity) <= 0 or len(quantity) >= 4) and type(quantity) != int:
                                    raise ValueError("quantity must be between 0 and 1000, inclusive")
                                raise TypeError("quantity must be an integer")
                        else:
                            if len(year) > 4 or len(year) < 4:
                                raise ValueError("year must be 4 digits exactly.")
                            raise TypeError("year must be a integer.")
                    else:
                        raise TypeError("ISBN must be an integer and between 4 and 20 digits, inclusive")
                else:
                    raise ValueError("Author is invalid")
            else:
                raise ValueError("There is no lower, uppercase letter(s) or spaces")
        else:
            raise ValueError('invalid order number')
    except ValueError as e:
        print("The ValueError is " + str(e))
    except TypeError as e:
        print("The TypeError is " + str(e))


def calculate_per_book_cost(cost, quantity):
    try:
        cost_per_book = cost / quantity
        return cost_per_book
    except ZeroDivisionError:
        return "The quantity cannot be zero"


def write_book_order_details(filename, title, author, isbn, year, quantity, cost, unit_cost):
    file_script = open(filename, "w")
    while True:
        try:
            if re.search(r"^[a-zA-Z0-9]{1,8}.txt$", filename):
                file_script.write('BOOK ORDER\n' +
                                  'title=' + title + '\n' +
                                  'author=' + author + '\n' +
                                  'isbn=' + isbn + '\n' +
                                  'year=' + year + '\n' +
                                  'quantity=' + quantity + '\n' +
                                  'cost=$' + cost + '\n' +
                                  'unit_cost=$' + unit_cost
                                  )
                file_script.close()
                break
            else:
                raise ValueError("this is a value error.")
        except FileExistsError:
            filename = input("Please enter another file name because it has already been used: ")
        except ValueError as e:
            print("The ValueError is " + str(e))
        except TypeError as e:
            print("The TypeError is " + str(e))

