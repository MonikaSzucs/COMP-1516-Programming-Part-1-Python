"""
Lab 9 by Monika Szucs A00878763
A script containing the main() function
:author: Monika Szucs
:date: November 1, 2021
"""


from functions import is_valid_bc_license_place, is_valid_python_variable_name, is_valid_email_address, is_valid_human_height


def main():
    print(is_valid_bc_license_place("ABC123"))
    print(is_valid_bc_license_place("123ABC"))
    print(is_valid_bc_license_place("AB1 23C"))
    print(is_valid_bc_license_place("AB1-23C"))
    print(is_valid_bc_license_place("A1B2C3"))

    is_valid_python_variable_name("first__name")
    is_valid_python_variable_name("x")
    is_valid_python_variable_name("a_good_variable_name")
    is_valid_python_variable_name("a*()Ther24")

    print(is_valid_email_address("Jason_Harrison@bcit.ca"))

    # print(is_valid_human_height("2'01\""))


if __name__ == "__main__":
    main()
