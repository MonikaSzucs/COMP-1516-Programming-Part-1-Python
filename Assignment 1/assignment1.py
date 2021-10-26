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
        letter_position = []
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
                skipped += 1
            for j in range(len(capital)):
                if skipped == 0:
                    if j > 0:
                        if number_position < len(letter_position):
                            if j == letter_position[number_position]:
                                single_capital.pop()
                                single_capital.append(capital[j-1].upper())
                                single_capital.append(capital[j].lower())
                                number_position += 1
                                if j < len(capital):
                                    if len(capital) - 1 == j:
                                        continue
                                    else:
                                        single_capital.append(capital[j+1].upper())
                                        skipped = 1
                                else:
                                    continue
                            elif j == len(capital) - 1:
                                single_capital.append(capital[j].lower())
                            else:
                                single_capital.append(capital[j].lower())
                        else:
                            single_capital.append(capital[j].lower())
                            number_position += 1
                    elif j == 0:

                        single_capital.append(capital[j].lower())
                    else:
                        single_capital.append(capital[j].lower())
                    pos += 1
                else:
                    skipped = 0
                    continue
        single_capital = ''.join(single_capital)
        case_capitals.append(single_capital)
    return case_capitals


def get_doubled_letter_countries():
    """
        A function that will only get the countries that have double letters and organize it by alphabet
        Fourth Variant
    """
    print("\n")
    print("Start get_doubled_letter_countries")
    double_letter_countries = []
    position = 0
    for country in countries:
        letter_position = 0
        for character in range(len(country)):
            if character < len(country):
                try:
                    if country[character] == country[character + 1]:
                        double_letter_countries.append(country.lower())
                except (TypeError, NameError, ValueError, IndexError):
                    continue
            letter_position += 1
        position += 1
    converted_tuple = tuple(sorted(double_letter_countries, key=lambda t: t[-3]))
    return converted_tuple


def main():
    print("I should not be called")


if __name__ == "__main__":
    main()
