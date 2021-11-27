"""
Assignment 3 by Monika Szucs A00878763
A script containing the main() function
:author: Monika Szucs
:date: November 23, 2021
"""
from Country import Country
from data import countries_and_capitals


def main():
    try:
        country = Country("Austria", "Vienna", 1000)
        print(country.print_details())
    except ValueError as v:
        print(str(v))



if __name__ == "__main__":
    main()

