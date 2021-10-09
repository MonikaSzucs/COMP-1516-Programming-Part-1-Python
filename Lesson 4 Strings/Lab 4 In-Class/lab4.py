import login


def main():
    info = ["first_name", "last_name"]
    spelling = ["first name", "last name"]
    print(len(info))
    print(info[0])
    i = 0

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
            print(first_name)
        elif info[i] == "last_name":
            last_name = names.title()
            print(last_name)

        i += 1

    print(len(first_name))
    print(len(last_name))

    if len(first_name) > 3:
        first_name_grabbed = first_name[0:3]
        print(first_name_grabbed)
    else:
        print(first_name)

    if len(last_name) > 3:
        last_name_grabbed = last_name[0:3]
        print(last_name_grabbed)
    else:
        print(last_name)

    bcit_id = input(" enter your BCIT ID: ")
    print(bcit_id)
    length = len(bcit_id)
    if length >= 3:
        bcit_id_grabbed = bcit_id[length - 3:]
        print(bcit_id_grabbed)

    concatenated_characters = first_name_grabbed + last_name_grabbed + bcit_id_grabbed
    print(concatenated_characters)


if __name__ == "__main__":
    main()
