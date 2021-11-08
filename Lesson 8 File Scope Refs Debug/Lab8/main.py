"""
Lab 8 by Monika Szucs A00878763
A script containing the main() function
:author: Monika Szucs
:date: November 7, 2021
"""

# importing the functions that are within the functions file
from functions import get_countries, get_capitals, get_file_data


def main():
    country_substring = input("Please enter a countries substring to see if we can find it: ")
    get_countries(country_substring)
    capitals_substring = input("Please enter a capitals substring to see if we can find it: ")
    get_capitals(capitals_substring)
    print()
    get_file_data()


if __name__ == "__main__":
    main()
