"""
Lab 9 by Monika Szucs A00878763
A script containing the is_valid_bc_license_place(license), is_valid_python_variable_name(variable),
is_valid_email_address(email), is_valid_human_height(height)
:author: Monika Szucs
:date: November 11, 2021
"""

import re


def is_valid_bc_license_plate(car_license):
    """
        A function that will return True or False if it matches the pattern of a license plate
        First Variant, parameters, return
        :param car_license: contains the car license plate
        :return: True if it matches any of the patterns or else returns False
    """
    if re.search("^[A-Z]{3}\\d{3}$|^\\d{3}[A-Z]{3}$|^[A-Z]{2}\\d ?\\d{2}[A-Z]$|^[A-Z]{2}\\d-\\d{2}[A-Z]$", car_license):
        return True
    else:
        return False


def is_valid_python_variable_name(variable):
    """
        A function that will return a match that is between one and 32 characters total which must be lowercase and/or a
        underscore but no more than one underscore in a row
        Second Variant and parameter
        :param variable: a variable entered in by the user for a variable name
        :return: True if it matches any of the patterns or else returns False
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
        A function that will return the correct height with the feet between 2 to 8, the inches between 0 to 11
        and cannot include 2 feet and 0 inches or anything above 8 feet and 11 inches
        Fourth Variant, parameters, return
        :param height: contains the height in feet and inches
        :return: True if it matches any of the patterns or else returns False
    """
    print()
    try:
        print(height)
        height_array = re.split("'", height)
        feet = height_array[0]
        inches = height_array[1]
        if re.search("[2-8]", feet):
            if (inches[-1] == '\"') or (re.search("[in]$", inches)):
                if inches[-1] == '\"':
                    inches_quote_removed = inches[:-1]
                    print(int(inches_quote_removed))
                    if re.search("^[0-9]$|^0[0-9]$|^1[01]$", inches_quote_removed):
                        if re.search("^[2]\'[0]\"$|^[2]\'[0]{2}\"$", height):
                            return False
                        else:
                            return True
                    else:
                        return False
                elif re.search("[in]$", inches):
                    inches_quote_removed = inches[:-2]
                    if re.search("^[0-9]$|^0[0-9]$|^1[01]$", inches_quote_removed):
                        if re.search("^[2]\'[0]in$|^[2]\'[0]{2}in$", height):
                            return False
                        else:
                            return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    except (TypeError, ValueError):
        return False
