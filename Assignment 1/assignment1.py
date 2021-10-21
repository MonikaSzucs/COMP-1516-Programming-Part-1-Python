"""
Assignment 1 by Monika Szucs, A00878763
"""
from data import countries_and_capitals, countries, capitals
import json


def print_json_countries_and_capitals():
    increment = 0
    print("[")
    while True:
        print("\t{")
        if increment < len(countries):
            print('\t\t"country_name" : ' + countries[increment])
            print('\t\t"capital_city" : ' + capitals[increment])
        else:
            break
        increment += 1
        print("\t}")
    print("]")


def get_list_of_countries_whose_nth_letter_is(n, letter):
    print("\n")
    print("get_list_of_countries_whose_nth_letter_is:")
    position = n - 1
    number = 0
    answer = []
    for country in countries:
        if letter == countries[number][position]:
            answer.append(country)
        number += 1
    return answer


def get_funny_case_capital_cities(letter):
    print("\n")
    case_capitals = []
    cap = 0
    number = 0
    position_within_list = list()
    for capital in capitals:
        print(capital)
        position_within_list.append(capital)
        for character in capital:
            print(character)
            if character == letter:
                letter.upper()
                case_capitals.append(capital)
        if cap < len(character):
            print("END")

    print(position_within_list)

    """
    answer = []
    working_on = ''
    for capital in capitals:
        position_within = 0
        position_within_list = ()
        print(capital)
        print(capital[position_within])
        while position_within < len(capital):
            print(position_within)
            if letter == capital[position_within].lower():
                print("IT IS MATCHING " + capital[position_within].lower())
                working_on += capital
                print(working_on)
                working_on = capital[:position_within - 1].lower() + capital[position_within - 1:].capitalize()
                working_on = capital[:position_within + 1].lower() + capital[position_within + 1:].capitalize()
                position_within += 1
                print(working_on)

            position_within += 1
            
    """
    print("get_funny_case_capital_cities:")
    #print(answer)




def get_doubled_letter_countries():
    pass


def main():
    print("I should not be called")


if __name__ == "__main__":
    main()
