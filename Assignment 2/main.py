from assignment2 import write_countries_capitals_to_file, save_capitals
import re
from data import countries_and_capitals, countries, capitals


def main():
    file_name = input("Please enter a file name: ")
    write_countries_capitals_to_file(file_name)
    save_capitals()


if __name__ == '__main__':
    main()


