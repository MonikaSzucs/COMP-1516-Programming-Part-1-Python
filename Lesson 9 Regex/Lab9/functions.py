"""
Lab 9 by Monika Szucs A00878763
A script containing the is_valid_bc_license_place(license), is_valid_python_variable_name(variable),
is_valid_email_address(email), is_valid_human_height(height)
:author: Monika Szucs
:date: November 1, 2021
"""

import re


def is_valid_bc_license_plate(license):
    """
        A function that will return True or False if it matches the pattern of a license plate
        First Variant, parameters, return
        :param license:
        :return: True if it matches any of the patterns or else returns False
    """
    if re.search("^[A-Z]{3}\\d{3}$|^\\d{3}[A-Z]{3}$|^[A-Z]{2}\\d ?\\d{2}[A-Z]$|^[A-Z]{2}\\d-\\d{2}[A-Z]$", license):
        return True
    else:
        return False


def is_valid_python_variable_name(variable):
    """
        A function that will return a match that is between one and 32 characters total which must be lowercase or
        underscore but no more than one underscore in a row
        Second Variant and parameter
        :param variable: a variable entered in by the user
    """
    print()
    print("is_valid_python_variable_name")
    print(variable)
    if re.search("^[a-z_]{1,32}$", variable):
        if not re.search("__", variable):
            print("passed")
            print("YES FOUND")
            print(variable)
        else:
            print("not found")
    else:
        print("NOT FOUND")
    print()


def is_valid_email_address(emails):
    """
        A function that will return the
        Third Variant, parameters, return
        :param emails:
        :return: True if it matches any of the patterns or else returns False
    """
    print()
    print("is_valid_email_address")
    print(emails)
    for email in emails:
        print(email)
        if re.search("^[a-zA-Z0-9_]{1,256}@[a-zA-Z0-9_]{1,32}\.[a-zA-Z]{2,5}$", email):
            if re.search("__", email) is None:
                print(email)


def is_valid_human_height(feet, inches):
    """
        A function that will return the
        Fourth Variant, parameters, return
        :param license:
        :return: True if it matches any of the patterns or else returns False
    """
    print()
    print(feet)
    print(inches)

    if re.search(".+?(?=\')", height):
        print("correct")
        if re.search("^[2]", height) == 2:
            print("first number is 2")
    else:
        print("incorrect")
