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


def is_valid_email_address(email):
    """
        A function that will return the
        Third Variant, parameters, return
        :param license:
        :return: True if it matches any of the patterns or else returns False
    """
    print()
    print("---")
    print("is_valid_email_address")
    print(email)

    split_email = re.findall(r'(.+)@(.+)\.(.+)', email)
    print(split_email)
    first_part_email = split_email[0][0]
    # Character length
    if re.search(r"^[a-zA-Z_]{1,256}$", first_part_email):
        print(first_part_email)
        # underscore
        if not re.match("^[_]", first_part_email):
            print("no underscore at beginning")
            if not re.search("[_]$", first_part_email):
                print("no underscore at the end")
            else:
                print("underscore at end error")
        else:
            print("underscore at beginning error")
    else:
        print("Too long")
    #domain_part_email = split_email[0][1]
    #print(domain_part_email)
    #ending_part_email = split_email[0][2]
    #print(ending_part_email)
    """
    if re.search(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        print("passed")
    else:
        print("failed")
    """


def is_valid_human_height(height):
    """
        A function that will return the
        Fourth Variant, parameters, return
        :param license:
        :return: True if it matches any of the patterns or else returns False
    """
    print()
    print(height)
    if re.search("^[2-8][']", height):
        print("correct")
    else:
        print("incorrect")


