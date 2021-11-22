"""
Lab 10 by Monika Szucs A00878763
A script containing the main() function
:author: Monika Szucs
:date: November 15, 2021
"""

import sys
import os
from aifc import Error
from book_order_utils import validate_book_order_details, calculate_per_book_cost, write_book_order_details


def check_data(param):
    # isinstance()
    # if not type(param) is str:
    #    raise TypeError("Parameter must be a string")
    if not isinstance(param, str):
        raise TypeError("Parameter must be a string")


def raise_error():
    value = int(input("Please enter a number: "))

    if value < 0:
        raise ValueError("Cannot have a negative number")


def main():
    # print(sys.argv)
    # print(sys.argv[0])
    # print(sys.argv[1])
    # print(sys.argv[2])
    # print(len(sys.argv))
    # num = 0
    # while num < len(sys.argv):
    #    print(sys.argv[num])
    #    num += 1

    # print(os.getenv())
    # print(os.getcwd())
    # path = os.getcwd()
    # print(os.path.isfile(path))
    # print(os.path.exists(path))
    # filename = "test.txt"
    # print(os.path.isfile(filename))
    # print(os.path.exists(filename))
    # full_path = os.path.join(path, filename)
    # print(full_path)

    try:
        # check_data(145)
        check_data("Hello")
        raise_error()
    except TypeError as t:
        print(t)
    except ValueError as v:
        print(v)
    except Error as e:
        print("Didn't  handle the specific error and now we are here")
        print(e)

    while True:
        try:
            raise_error()
            break
        except ValueError as v:
            print(v)


if __name__ == '__main__':
    main()