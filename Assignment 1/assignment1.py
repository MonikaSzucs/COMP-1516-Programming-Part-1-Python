"""
Assignment 1 by Monika Szucs, A00878763
"""
from data import countries_and_capitals, countries, capitals
import json


def print_json_countries_and_capitals():
    print(countries)
    x = {}
    increment = 0
    while True:
        if increment < len(countries):
            x.update({"country_name": countries[increment],
                      "capital_city": capitals[increment]
                      })
        else:
            break
        increment += 1
    print(x)




def get_list_of_countries_whose_nth_letter_is(n,letter):
    pass


def get_funny_case_capital_cities(letter):
    pass


def get_doubled_letter_countries():
    pass


def main():
    print("I should not be called")


if __name__ == "__main__":
    main()
