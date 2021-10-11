import re


def generate_login(first_name, last_name, bcit_id):
    print(first_name)
    print(last_name)
    print(bcit_id)


def change_password():
    print("enter a new password. The password should be at least 7 characters long has one uppercase, "
        "one lowercase character and one number. It cannot have special characters")

    new_password = input("enter a new password: ")

    # Cannot have special characters
    special_characters_boolean = False
    special_characters = new_password.isalnum()
    print(special_characters)
    while True:
        if len(new_password) >= 7:
            special_characters = new_password.isalnum()
            if not special_characters:
                new_password = input("special characters are not allowed: ")
            else:
                # Checks for at least one digit
                d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
                for c in new_password:
                    if c.isupper():
                        d["UPPER_CASE"] += 1
                    elif c.islower():
                        d["LOWER_CASE"] += 1
                    else:
                        pass
                print("Original String : ", new_password)
                print("No. of Upper case characters : ", d["UPPER_CASE"])
                print("No. of Lower case Characters : ", d["LOWER_CASE"])
                if d["UPPER_CASE"] >= 1:
                    print("Found at least one uppercase")
                    if re.search(r'\d', new_password):
                        # <_sre.SRE_Match at 0x1070055e0>
                        print("Found at least one digit")
                        if d["LOWER_CASE"] >= 1:
                            print("Found at least one lowercase")
                            break
                        else:
                            print("Please have at least one lowercase letter")
                            new_password = input("enter a new password: ")
                    else:
                        print("must have at least one digit")
                        new_password = input("enter a new password: ")
                else:
                    print("Password must have at least one uppercase character")
                    new_password = input("enter a new password: ")
        else:
            print("Password must be longer than 7 characters")
            new_password = input("enter a new password: ")

    print(" valid password")
    print(new_password)





