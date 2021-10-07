import login


def main():
    first_name = input('enter your first name: ').split()
    while True:
        if True:
            first_name = input('Please enter only alphabetical characters for your name: ').split()

            while len(first_name) > 1:
                first_name = input('Please Enter only one word').split()
            print(type(first_name))
            first_name = ''.join(map(str, first_name))
            first_name = first_name.title()
            if first_name.isalpha():
                last_name = input("enter your last name: ").title()
                bcit_id = input(" enter your BCIT ID")
                login.generate_login(first_name, last_name, bcit_id)
                break
        else:
            print("Please enter only alphabetical characters for your name.")



if __name__ == "__main__":
    main()

