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

        # Print Details
        for country in countries_and_capitals:
            print(country)
            random_value = random.randint(1000000, 1000000000)
            all_countries.append([country[0], country[1], random_value])
            country = Country(country[0], country[1], random_value)
            print(country.print_details())
        print(all_countries)
        print()

        # Birth
        for country in all_countries:
            print(country)
            population_number = country[2]
            country.pop(2)
            grabbed_country = Country(country[0], country[1], population_number)
            calculated_country = grabbed_country.birth()
            country.append(calculated_country)
            grabbed_country_updated = Country(country[0], country[1], country[2])
            print(grabbed_country_updated.print_details())
        print(all_countries)
        print()

        # Death
        for country in all_countries:
            print(country)
            population_number = country[2]
            country.pop(2)
            grabbed_country = Country(country[0], country[1], population_number)
            calculated_country = grabbed_country.death(1)
            print(grabbed_country.print_details())
            country.append(calculated_country)
            print(country)
        print(all_countries)
        print()

        # Disaster
        for country in all_countries:
            print(country)
            population_number = country[2]
            country.pop(2)
            grabbed_country = Country(country[0], country[1], population_number)
            calculated_country = grabbed_country.disaster(100000000)
            print(grabbed_country.print_details())
            country.append(calculated_country)
            print(country)
        print(all_countries)

    except ValueError as v:
        print(str(v))


if __name__ == "__main__":
    main()

