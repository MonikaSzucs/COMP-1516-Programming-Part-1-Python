"""
Lab 10 by Monika Szucs A00878763
A script containing the main() function
:author: Monika Szucs
:date: November 15, 2021
"""

import sys
from book_order_utils import validate_book_order_details, calculate_per_book_cost, write_book_order_details


def main():
    print(sys.argv)
    length_argument = len(sys.argv) - 1
    start = 1
    print()
    while start <= length_argument:
        print(sys.argv[start])
        start += 1


if __name__ == '__main__':
    main()

