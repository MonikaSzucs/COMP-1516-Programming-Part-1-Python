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
    position_within = 0
    position = 0
    letter_position = 0
    position_within_list = list()
    for capital in capitals:
        print(capital)
        position_within_list.append(capital)
        print(position_within_list)
        print(position_within_list[position])
        print(len(position_within_list[position]))
        while position_within < len(position_within_list[position]):
            print("inside while loop")
            print(position_within)
            print(position_within_list[position])
            print(position_within_list[position][letter_position])
            if letter == position_within_list[position][letter_position].lower():
                print("inside if statement")
                print(letter)
                print(position_within)
                position_within_list[position][letter_position - 1].upper()
                print(position_within_list[position][letter_position-1].upper())


            position_within += 1
            letter_position += 1
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
