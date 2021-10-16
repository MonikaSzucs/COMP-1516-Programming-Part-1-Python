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
    return total


def get_list_of_countries_whose_nth_letter_is(n, letter):
    position = n - 1
    number = 0
    answer = []
    for country in countries:
        if letter == countries[number][position]:
            answer.append(countries[number])
        number += 1
    print("get_list_of_countries_whose_nth_letter_is:")
    return answer


def get_funny_case_capital_cities(letter):
    print("START")
    print(letter)
    print(capitals)
    answer = []
    working_on = ''
    for capital in capitals:
        position_within = 0
        print(capital)
        print(capital[position_within])
        while position_within < len(capital):
            print(position_within)
            if letter == capital[position_within].lower():
                print("IT IS MATCHING" + capital[position_within].lower())
                working_on += capital
                print(working_on)
                working_on = capital[:position_within - 1].lower() + capital[position_within - 1:].capitalize()

                print(working_on)

            position_within += 1
    print("get_funny_case_capital_cities:")
    print(answer)




def get_doubled_letter_countries():
    pass


def main():
    print("I should not be called")


if __name__ == "__main__":
    main()
