"""
Assignment 1 by Monika Szucs, A00878763
"""
from data import countries_and_capitals, countries, capitals
import json


def print_json_countries_and_capitals():
    increment = 0
    total = []
    while True:
        if increment < len(countries):
            pair = {"country_name": countries[increment],
                    "capital_city": capitals[increment]
                    }
            total.append(pair)
        else:
            break
        increment += 1
    print("print_json_countries_and_capitals")
    print(total)


def get_list_of_countries_whose_nth_letter_is(n, letter):
    position = n - 1
    number = 0
    answer = []
    for country in countries:
        if letter == countries[number][position]:
            answer.append(countries[number])
        number += 1
    print(answer)


def get_funny_case_capital_cities(letter):
    print(letter)
    print(capitals)
    position = 0
    number = 0
    answer = []
    for capital in capitals:
        print(capital)
        print(capital[number])
        if letter == capitals[number][position]:
            answer.append(capitals[number])
        number += 1
    print(answer)




def get_doubled_letter_countries():
    pass


def main():
    print("I should not be called")


if __name__ == "__main__":
    main()
