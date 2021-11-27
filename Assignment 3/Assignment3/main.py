"""
Assignment 3 by Monika Szucs A00878763
A script containing the main() function
:author: Monika Szucs
:date: November 23, 2021
"""
from Country import Country
from data import countries_and_capitals
import random


def main():
    try:
        all_countries = []
        for country in countries_and_capitals:
            print(country)
            random_value = random.randint(1000000, 1000000000)
            #random_value = random.randint(1000000, 2000000)
            all_countries.append([country[0], country[1], random_value])
            country = Country(country[0], country[1], random_value)
            print(country.print_details())
            #input("Press enter to check the next country")
        print(all_countries)

        for country in all_countries:
            print(country)
            print(country[2])
            population_number = country[2]
            print(type(population_number))
            country = Country(country[0], country[1], population_number)
            print(country.birth())

    except ValueError as v:
        print(str(v))



if __name__ == "__main__":
    main()

