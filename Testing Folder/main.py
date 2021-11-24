import re


def get_input():
    while True:
        data = input("Please Enter a Four Digit Integer: ")
        if re.search("^\d{4}$", data) is None:
            print("Input must be a four digit integer")
        else:
            return data


def main():
    print(get_input())


if __name__ == "__main__":
    main()
