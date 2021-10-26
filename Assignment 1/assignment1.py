"""
Assignment 1 by Monika Szucs A00878763
A script containing print_json_countries_and_capitals(), get_list_of_countries_whose_nth_letter_is(n, letter),
get_funny_case_capital_cities(letter), get_doubled_letter_countries(), and a dummy main()
:author: Monika Szucs
:date: October 25, 2021
"""
from itertools import count

from data import countries_and_capitals, countries, capitals
import json
import re


def print_json_countries_and_capitals():
    """
        A function that will print out the countries and capitals in a json format.
        First Variant
    """
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
    """
        A function that will take two parameters. It will then check to see if that country contains that letter at
        that position.
        Second Variant, parameters, return
        :param n: check nth position
        :param letter: containing the letter
        :return: returns the list of countries who's nth letter matches the letter of the parameter
    """
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
    """
    A function that will take a parameter and checks to see if a letter is found in the capital city and if so it will
    make the previous letter within uppercase and then next letter within uppercase.
    Third Variant, parameter, return
    :param letter: contains a letter
    :return: returns all cities that contain that letter and is stored in a list
    """
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
    return case_capitals


def get_doubled_letter_countries():
    """
        A function that will only get the countries that have double letters and organize it by alphabet
        Fourth Variant
    """
    print("Start get_doubled_letter_countries")
    double_letter_countries = []
    position = 0
    for country in countries:
        print(country)
        letter_position = 0
        for character in range(len(country)):
            print("START SECOND LOOP")
            print(character)
            print(country)
            print(country[character])
            print(len(country))
            if character < len(country):
                print("LESS")
                try:
                    if country[character] == country[character + 1]:
                        print("MATCHING!!!")
                        double_letter_countries.append(country.lower())
                        print("There is an error")
                except (TypeError, NameError, ValueError, IndexError):
                    print("IndexError it means it is ending")
            letter_position += 1
        position += 1
    print("END")
    print(double_letter_countries)
    print(sorted(double_letter_countries, key=lambda t: t[-3]))


def main():
    print("I should not be called")


if __name__ == "__main__":
    main()
