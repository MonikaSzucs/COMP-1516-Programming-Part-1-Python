import login


def main():
    start = "first"
    first_name = input('enter your first name: ').split()
    while True:
        if start == "first":
            first_name = ''.join(map(str, first_name))
            first_name = first_name.title()
            if first_name.isalpha():
                break
            elif len(first_name) > 1:
                start = "incorrect spacing"
                continue
            else:
                start = "incorrect"
                continue
        elif start == "incorrect":
            first_name = input('Please enter only alphabetical characters for your first name: ').split()
            while len(first_name) > 1:
                first_name = input('Please enter only one word').split()
                continue
            first_name = ''.join(map(str, first_name))
            first_name = first_name.title()
            if first_name.isalpha():
                break
            else:
                start = "correct"
                continue
        elif start == "incorrect spacing":
            first_name = input('There was incorrect spacing. We only need your first name: ').split()
            while len(first_name) > 1:
                first_name = input('Please enter only one word').split()
                continue
            first_name = ''.join(map(str, first_name))
            first_name = first_name.title()
            if first_name.isalpha():
                break
            else:
                start = "incorrect"

        elif name == "correct":
            first_name = input('enter your first name: ').split()
            first_name = ''.join(map(str, first_name))
            first_name = first_name.title()
            if first_name.isalpha():
                break

        print(type(first_name))
        print(start)

    print(first_name)





if __name__ == "__main__":
    main()

