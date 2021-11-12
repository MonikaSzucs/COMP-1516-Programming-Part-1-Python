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

    print(is_valid_python_variable_name("first_name"))
    print(is_valid_python_variable_name("first__name"))
    print(is_valid_python_variable_name(
        "first_namesfsdfklwenvlkjdcmslwsdjkfdsfsajfldasgmlreagkjdsljgldsvvcmdaskfvjdakljvdmaclwaekjldksjgldsjagfldjsafkljdsalkmclvmvkfdjagkdgldjalkfdlsmcldsjafsdljfldajgfa"))
    print(is_valid_python_variable_name("x"))
    print(is_valid_python_variable_name("a_good_variable_name"))
    print(is_valid_python_variable_name("a*()Ther24"))
    print(is_valid_python_variable_name("Monika"))

    print(is_valid_email_address("Jason_Harrison@bcit.ca"))
    print(is_valid_email_address("a_____b@c.com"))
    print(is_valid_email_address("$$$testing@hotmail.com"))
    print(is_valid_email_address("hello____world@gmail.com"))
    print(is_valid_email_address("myemail@shaw.ca"))
    print(is_valid_email_address("willthiswork@IdontKNow.community"))
    print(is_valid_email_address("123"))
    print(is_valid_email_address("this is the way"))
    print(is_valid_email_address("mlinder_3@bcit.ca"))
    print(is_valid_email_address("hello@something"))
    print(is_valid_email_address("a@x.z"))
    print(is_valid_email_address("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.ccccccccccccccccccccccccccccccc"))
    print(is_valid_email_address("_Monika@hotmail.com"))
    print(is_valid_email_address("Monika_@hotmail.com"))


    is_valid_human_height("2'01")


if __name__ == "__main__":
    main()
