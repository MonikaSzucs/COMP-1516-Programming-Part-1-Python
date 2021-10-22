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
    print("get_funny_case_capital_cities:")
    case_capitals = []

    for capital in capitals:
        letter_position = []
        print(capital)
        for i in range(len(capital)):
            print(i)
            print(capital[i])
            if capital[i].lower() == letter.lower():
                letter_position.append(i)
        print(letter_position)
        single_capital = []
        print("second for loop")
        pos = 0
        for j in range(len(capital)):
            print(j)
            print(letter_position)
            print(capital[j])
            if j > 0:
                if len(capital) < (j + 1):
                    print(capital[j].lower())
                    single_capital.append(capital[j].lower())
            pos += 1
        print(single_capital)



        # for character in capital:
        """    print(character)
            print(capital[character_count])
            if character.lower() == letter.lower():
                number += 1
                letter.upper()
                if number == 1:
                    case_capitals.append(capital)
            cap += 1
            character_count += 1
        print(cap)
        print(len(capital))
        if cap >= len(capital):
            print("END")
        print(case_capitals)"""




def get_doubled_letter_countries():
    pass


def main():
    print("I should not be called")


if __name__ == "__main__":
    main()
