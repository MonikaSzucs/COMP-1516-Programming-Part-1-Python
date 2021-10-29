import re


def is_valid_bc_license_place(license):
    if re.findall("^[A-Z][A-Z][A-Z][0-9][0-9][0-9]|^[0-9][0-9][0-9][A-Z][A-Z][A-Z]|^[A-Z][A-Z][0-9] ?[0-9][0-9][A-Z]|^[A-Z][A-Z][0-9]-[0-9][0-9][A-Z]", license):
        return True
    else:
        return False


def is_valid_python_variable_name(variable):
    print()
    print(variable)


def is_valid_email_address(email):
    print()
    print(email)


def is_valid_human_height(height):
    print()
    print(height)


