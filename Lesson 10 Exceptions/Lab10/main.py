"""
Lab 10 by Monika Szucs A00878763
A script containing the main() function
:author: Monika Szucs
:date: November 15, 2021
"""

from book_order_utils2 import validate_book_order_details, calculate_per_book_cost, write_book_order_details


def main():
    validate_book_order_details("0021", "The title here", "Monika Szucs", "12345458346", "2012", "10", "20.0")
    #validate_book_order_details("0021", "The Title Here", "Monika's24", "12345458346", "2012", "10", 20.01)
    #print(calculate_per_book_cost(12.00, 2))
    #print(calculate_per_book_cost(12.00, 0))
    #filename = input("Please enter a file name: ")
    #write_book_order_details(filename, "Intro to Python", "Bill Smith", 123456, 2010, 10, 500.50, 50.05)

if __name__ == "__main__":
    main()
