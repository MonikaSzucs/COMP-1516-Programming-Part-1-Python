"""
Lab 9 by Monika Szucs A00878763
A script containing the is_valid_bc_license_place(license), is_valid_python_variable_name(variable),
is_valid_email_address(email), is_valid_human_height(height)
:author: Monika Szucs
:date: November 1, 2021
"""


import re


def is_valid_bc_license_place(license):
    """
        A function that will return the
        First Variant, parameters, return
        :param license:
        :return: True if it matches any of the patterns or else returns False
    """
    if re.findall("^[A-Z][A-Z][A-Z][0-9][0-9][0-9]|^[0-9][0-9][0-9][A-Z][A-Z][A-Z]|^[A-Z][A-Z][0-9] ?[0-9][0-9][A-Z]|^[A-Z][A-Z][0-9]-[0-9][0-9][A-Z]", license):
        return True
    else:
        return False


def is_valid_python_variable_name(variable):
    """
        A function that will return the
        Second Variant, parameters, return
        :param license:
        :return: True if it matches any of the patterns or else returns False
    """
    print()
    print(variable)


def is_valid_email_address(email):
    """
        A function that will return the
        Third Variant, parameters, return
        :param license:
        :return: True if it matches any of the patterns or else returns False
    """
    print()
    print(email)


def is_valid_human_height(height):
    """
        A function that will return the
        Fourth Variant, parameters, return
        :param license:
        :return: True if it matches any of the patterns or else returns False
    """
    print()
    print(height)


