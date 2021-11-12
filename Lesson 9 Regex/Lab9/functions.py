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
        A function that will return a match that is between one and 32 characters total which must be lowercase and/or a
        underscore but no more than one underscore in a row
        Second Variant and parameter
        :param variable: a variable entered in by the user for a variable name
    """
    print()
    print("is_valid_python_variable_name")
    print(variable)
    if re.search("^[a-z_]{1,32}$", variable):
        if not re.search("__", variable):
            return True
        else:
            return False
    else:
        return False
    print()


def is_valid_email_address(email):
    """
        A function that will return if the email matches the specifications with True or False if doesn't
        Third Variant, parameters, return
        :param email: checks to see if email entered fits the rules within this function
        :return: True if it matches any of the patterns or else returns False
    """
    print()
    print("is_valid_email_address")
    print(email)
    if re.search("^[a-zA-Z_]{1,256}@[a-zA-Z_]{1,32}\.[a-zA-Z]{2,5}$", email):
        email_data = re.split("@", email)
        username = email_data[0]
        if not (username[0] == "_" or username[-1] == "_"):
            print(email)
            return True
        else:
            return False
    else:
        return False


def is_valid_human_height(height):
    """
        A function that will return the
        Fourth Variant, parameters, return
        :param license:
        :return: True if it matches any of the patterns or else returns False
    """
    print()
    print(height)
    height_array = re.split("'", height)
    print(height_array[0])
    print(type(height_array[0]))
    print(height_array[0])
    print(height_array[1])
    

