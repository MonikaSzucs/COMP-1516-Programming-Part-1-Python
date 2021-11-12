"""
Lab 9 by Monika Szucs A00878763
A script containing the main() function
:author: Monika Szucs
:date: November 11, 2021
"""

from functions import is_valid_bc_license_plate, is_valid_python_variable_name, is_valid_email_address, \
    is_valid_human_height


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

    print(is_valid_human_height("2'01\""))
    print(is_valid_human_height("2'0\""))
    print(is_valid_human_height("2'00\""))
    print(is_valid_human_height("1'01\""))
    print(is_valid_human_height("2'd1\""))
    print(is_valid_human_height("d'01\""))
    print(is_valid_human_height("2'd1in"))
    print(is_valid_human_height("d'01in"))
    print(is_valid_human_height("2'1\""))
    print(is_valid_human_height("5'09\""))
    print(is_valid_human_height("6'2in"))
    print(is_valid_human_height("4'10in"))
    print(is_valid_human_height("2'0in"))
    print(is_valid_human_height("2'00in"))
    print(is_valid_human_height("6'2\""))
    print(is_valid_human_height("8'01\""))
    print(is_valid_human_height("8'11\""))
    print(is_valid_human_height("8'12\""))
    print(is_valid_human_height("8'11in"))
    print(is_valid_human_height("8'12in"))
    print(is_valid_human_height("9'01\""))


if __name__ == "__main__":
    main()
