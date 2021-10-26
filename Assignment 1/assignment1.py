"""
Assignment 1 by Monika Szucs, A00878763
"""
from itertools import count

from data import countries_and_capitals, countries, capitals
import json
import re


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
        print("STARTING FOR LOOP")
        letter_position = []
        print(capital)
        number_position = 0
        for i in range(len(capital)):
            if capital[i].lower() == letter.lower():
                letter_position.append(i)
        single_capital = []
        pos = 0
        skipped = 0
        if len(letter_position) == 0:
            continue
        else:
            if letter_position[0] == 0:
                single_capital.append(capital[0].lower())
                single_capital.append(capital[0+1].upper())
                print(single_capital)
                skipped += 1
            for j in range(len(capital)):
                print(skipped)
                print("START INTERNAL FOR LOOP")
                if skipped == 0:
                    if j > 0:
                        print("number position of letter that is matched")
                        print(letter_position)
                        print(number_position)
                        if number_position < len(letter_position):
                            print("letter position IN HERE")
                            if j == letter_position[number_position]:
                                print("inside if")
                                print(letter_position[number_position])
                                single_capital.pop()
                                single_capital.append(capital[j-1].upper())
                                print(capital[j].lower())
                                single_capital.append(capital[j].lower())
                                number_position += 1
                                if j < len(capital):
                                    print("inside if statement")
                                    print(len(capital))
                                    print(j)
                                    if len(capital) - 1 == j:
                                        print("last item in list")
                                    else:
                                        single_capital.append(capital[j+1].upper())
                                        print(single_capital)
                                        skipped = 1
                                else:
                                    print("inside else statmeent inside second loop")
                                    continue
                            elif j == len(capital) - 1:
                                print("last letter")
                                single_capital.append(capital[j].lower())
                            else:
                                print("INSIDE THIS ELSE STATEMENT")
                                single_capital.append(capital[j].lower())
                        else:
                            single_capital.append(capital[j].lower())
                            number_position += 1
                    elif j == 0:

                        single_capital.append(capital[j].lower())
                        print("initial position")
                    else:
                        single_capital.append(capital[j].lower())
                    pos += 1
                else:
                    skipped = 0
                    continue
        print(single_capital)
        single_capital = ''.join(single_capital)
        print(single_capital)
        case_capitals.append(single_capital)
        print("case_capitals")
        print(case_capitals)



def get_doubled_letter_countries():
    check_string = "google"
    for s in check_string:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1

    for key in count:
        if count[key] > 1:
            print
            key, count[key]


def main():
    print("I should not be called")


if __name__ == "__main__":
    main()
