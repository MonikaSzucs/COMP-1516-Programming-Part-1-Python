"""
A script with the main function used to call all the other functions
:author: Monika Szucs
:date: October 12, 2021
"""
# import login module
import login


def main():
    """
        The main function that gets the users First Name, Last Name and BCIT ID.
        Then sends the information to login.generate_login with 3 parameters and then creates the login information
        Main
    """
    info = ["first_name", "last_name"]
    spelling = ["first name", "last name"]
    i = 0

    # Grabbing the First and Last name of the user but making sure it is only alphabets with no spacing
    # grabbing the BCIT ID then sending it to the login.
    for names in info:
        # First Name
        start = "first"
        names = input('enter your %s: ' % (spelling[i])).split()
        while True:
            if start == "first":
                names = ''.join(map(str, names))
                names = names.title()
                if names.isalpha():
                    break
                elif len(names.split()) > 1:
                    start = "incorrect spacing"
                    continue
                else:
                    start = "incorrect"
                    continue
            elif start == "incorrect":
                names = input('Please enter only alphabetical characters for your %s: ' % (spelling[i])).split()
                while len(names) > 1:
                    names = input('Please enter only one word: ').split()
                    continue
                names = ''.join(map(str, names))
                names = names.title()
                if names.isalpha():
                    break
                elif len(names.split()) > 1:
                    start = "incorrect spacing"
                    continue
                else:
                    start = "incorrect"
                    continue
            elif start == "incorrect spacing":
                names = input('There was incorrect spacing. We only need your %s: ' % (spelling[i])).split()
                while len(names) > 1:
                    names = input('Please enter only one word: ').split()
                    continue
                names = ''.join(map(str, names))
                names = names.title()
                if names.isalpha():
                    break
                else:
                    start = "incorrect"

            elif start == "correct":
                names = input('enter your %s: ' % (spelling[i])).split()
                names = ''.join(map(str, names))
                names = names.title()
                if names.isalpha():
                    break

        if info[i] == "first_name":
            first_name = names.title()
        elif info[i] == "last_name":
            last_name = names.title()

        i += 1

    if len(first_name) >= 3:
        first_name_grabbed = first_name[0:3]
    else:
        first_name_grabbed = first_name

    if len(last_name) >= 3:
        last_name_grabbed = last_name[0:3]
    else:
        last_name_grabbed = last_name

    bcit_id = input(" enter your BCIT ID: ")
    length = len(bcit_id)
    if length >= 3:
        bcit_id_grabbed = bcit_id[length - 3:]

    default_password = login.generate_login(first_name_grabbed, last_name_grabbed, bcit_id_grabbed)

    # show the default password
    print(default_password)

    # generate a new password now
    login.change_password()


if __name__ == "__main__":
    main()
