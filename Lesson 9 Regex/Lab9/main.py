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

    is_valid_python_variable_name("first_name")
    is_valid_python_variable_name("first__name")
    is_valid_python_variable_name("first_namesfsdfklwenvlkjdcmslwsdjkfdsfsajfldasgmlreagkjdsljgldsvvcmdaskfvjdakljvdmaclwaekjldksjgldsjagfldjsafkljdsalkmclvmvkfdjagkdgldjalkfdlsmcldsjafsdljfldajgfa")
    is_valid_python_variable_name("x")
    is_valid_python_variable_name("a_good_variable_name")
    is_valid_python_variable_name("a*()Ther24")

    is_valid_email_address("Jason_Harrison@bcit.ca")
    is_valid_email_address("a_____b@c.com")
    is_valid_email_address("monika@hotmail.ca")
    is_valid_email_address("first_namesfsdfklwenvlkjdcmslwsdjkfdsfsajfldasgmlreagkjdsljgldsvvcmdaskfvjfirst_namesfsdfklwenvlkjdcmslwsdjkfdsfsajfldasgmlreagkjdsljgldsvvcmdaskfvfirst_namesfsdfklwenvlkjdcmslwsdjkfdsfsajfldasgmlreagkjdsljgldsvvcmdaskfvjfirst_namesfsdfklfdsggsdfdsfdsfsdfd@hotmail.com")
    is_valid_email_address("first_namesfsdfklwenvlkjdcmslwsdj23kfdsfsajfldasgmlreagkjdsljgldsvvcmdaskfvjfirst_namesfsdfklwenvlkjdcmslwsdjkfdsfsajfldasgmlreagkjdsljgldsvvcmdaskfvfirst_namesfsdfklwenvlkjdcmslwsdjkfdsfsajfldasgmlreagkjdsljgldsvvcmdaskfvjfirst_namesfsdfklfdsggsdfdsfdsfsdfd@hotmail.com")
    is_valid_email_address("_cmslwsdj23kfdsfsajfldasgmlreagkjdsljgldsjdcmslwsdjkfdsfsajfldasgmlreagkjdsljgldsvvcmdaskfvfirst_namesfsdfklwenvlkjdcmslwsdjkfdsfsajfldasgmlreagkjdsljgldsvvcmdaskfvjfirst_namesfsdfklfdsggsdfdsfdsfsdfd@hotmail.com")
    #is_valid_email_address("first_namesfsdfklwenvlkjdcmslwsdjkfdsfsajfldasgmlreagkjdsljgldsvvcmdaskfvjfirst_namesfsdfklwenvlkjdcmslwsdjkfdsfsajfldasgmlreagkjdsljgldsvvcmdaskfvfirst_namesfsdfklwenvlkjdcmslwsdjkfdsfsajfldasgmlreagkjdsljgldsvvcmdaskfvjfirst_namesfsdfklfdsggsdfdsfdsfsdf_@hotmail.com")

    #is_valid_email_address("mszucs1@my.bcit.ca")
    #is_valid_email_address("12345sdfsdf.com")

    is_valid_human_height('2’1”')


if __name__ == "__main__":
    main()
