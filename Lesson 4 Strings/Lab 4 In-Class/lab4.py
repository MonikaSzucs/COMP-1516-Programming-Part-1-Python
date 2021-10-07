import login


def main():
    info = ["first_name", "last_name"]
    print(len(info))
    print(info[0])

    for names in info:
        # First Name
        start = "first"
        info[names] = input('enter your first name: ').split()
        while True:
            if start == "first":
                info[names] = ''.join(map(str, info[names]))
                info[names] = info[names].title()
                if info[names].isalpha():
                    break
                elif len(info[names].split()) > 1:
                    start = "incorrect spacing"
                    continue
                else:
                    start = "incorrect"
                    continue
            elif start == "incorrect":
                info[names] = input('Please enter only alphabetical characters for your first name: ').split()
                while len(info[names]) > 1:
                    info[names] = input('Please enter only one word: ').split()
                    continue
                info[names] = ''.join(map(str, info[names]))
                info[names] = info[names].title()
                if info[names].isalpha():
                    break
                elif len(info[names].split()) > 1:
                    start = "incorrect spacing"
                    continue
                else:
                    start = "incorrect"
                    continue
            elif start == "incorrect spacing":
                info[names] = input('There was incorrect spacing. We only need your first name: ').split()
                while len(info[names]) > 1:
                    info[names] = input('Please enter only one word: ').split()
                    continue
                info[names] = ''.join(map(str, info[names]))
                info[names] = info[names].title()
                if info[names].isalpha():
                    break
                else:
                    start = "incorrect"

            elif start == "correct":
                info[names] = input('enter your first name: ').split()
                info[names] = ''.join(map(str, info[names]))
                info[names] = info[names].title()
                if info[names].isalpha():
                    break

            print(type(info[names]))
            print(start)

        print(info[0])






if __name__ == "__main__":
    main()

