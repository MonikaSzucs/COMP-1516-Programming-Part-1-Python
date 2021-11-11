"""
Lab 9 by Monika Szucs A00878763
A script containing the main() function
:author: Monika Szucs
:date: November 1, 2021
"""

from functions import is_valid_bc_license_plate, is_valid_python_variable_name, is_valid_email_address, \
    is_valid_human_height
from data import emails


def main():
    print(is_valid_bc_license_plate("ABC123"))
    print(is_valid_bc_license_plate("123ABC"))
    print(is_valid_bc_license_plate("AB1 23C"))
    print(is_valid_bc_license_plate("AB1-23C"))
    print(is_valid_bc_license_plate("A1B2C3"))

    is_valid_python_variable_name("first_name")
    is_valid_python_variable_name("first__name")
    is_valid_python_variable_name(
        "first_namesfsdfklwenvlkjdcmslwsdjkfdsfsajfldasgmlreagkjdsljgldsvvcmdaskfvjdakljvdmaclwaekjldksjgldsjagfldjsafkljdsalkmclvmvkfdjagkdgldjalkfdlsmcldsjafsdljfldajgfa")
    is_valid_python_variable_name("x")
    is_valid_python_variable_name("a_good_variable_name")
    is_valid_python_variable_name("a*()Ther24")

    is_valid_email_address(emails)

    feet, inches = input("Please first enter the feet then inches for the height: ").split()
    is_valid_human_height(feet, inches)


if __name__ == "__main__":
    main()
