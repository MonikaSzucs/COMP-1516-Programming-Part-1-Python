"""
Assignment 3 by Monika Szucs A00878763
A script containing the main() function and importing the two files data and Country
:author: Monika Szucs
:date: November 28, 2021
"""
from Country import Country
from data import countries_and_capitals
import random


def main():
    try:
        all_countries = []

        # Print Details
        print("Print Details Start")
        for country in countries_and_capitals:
            print(country)
            random_value = random.randint(1000000, 1000000000)
            all_countries.append([country[0], country[1], random_value])
            country = Country(country[0], country[1], random_value)
            print(country.print_details())
        print(all_countries)
        print("Print Details End")
        print()

        # Birth
        print("Birth Start")
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
        print("Birth End")
        print()

        # Death
        print("Death Start")
        for country in all_countries:
            print(country)
            population_number = country[2]
            country.pop(2)
            grabbed_country = Country(country[0], country[1], population_number)
            calculated_country = grabbed_country.death(1)
            country.append(calculated_country)
            grabbed_country_updated = Country(country[0], country[1], country[2])
            print(grabbed_country_updated.print_details())
        print(all_countries)
        print("Death End")
        print()

        # Disaster
        print("Disaster Start")
        for country in all_countries:
            print(country)
            population_number = country[2]
            country.pop(2)
            grabbed_country = Country(country[0], country[1], population_number)
            calculated_country = grabbed_country.disaster(100000000)
            country.append(calculated_country)
            grabbed_country_updated = Country(country[0], country[1], country[2])
            print(grabbed_country_updated.print_details())
        print(all_countries)
        print("Disaster End")

    except ValueError as v:
        print(str(v))


if __name__ == "__main__":
    main()

