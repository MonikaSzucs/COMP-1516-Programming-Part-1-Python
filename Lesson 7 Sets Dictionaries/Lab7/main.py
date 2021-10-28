"""
Assignment 1 by Monika Szucs A00878763
A script containing the original main() function
:author: Monika Szucs
:date: October 25, 2021
"""

import utilities_sets
import utilities_dict


def main():
    set1 = {"apple", "banana", "orange", "peach"}
    set2 = {"banana", "pineapple", "peach", "watermelon"}
    print(utilities_sets.get_total_items(set1))
    utilities_sets.display_all_items(set1)
    utilities_sets.add_item(set1, "cantaloupe")
    print(utilities_sets.remove_item(set1, "cantaloupe"))
    print()
    print(utilities_sets.get_the_union_of(set1, set2))

    canadian_provinces_and_capital_cities = {
        "Ontario": "Toronto",
        "Quebec": "Quebec City",
        "Nova Scotia": "Halifax",
        "New Brunswick": "Fredericton",
        "Manitoba": "Winnipeg",
        "British Columbia": "Victoria",
        "Price Edward Island": "Charlottetown",
        "Saskatchewan": "Regina",
        "Alberta": "Edmonton",
        "Newfoundland and Labrador": "St. John's"
    }

    utilities_dict.display_all(canadian_provinces_and_capital_cities)
    utilities_dict.get_capital_city("British Columbia", canadian_provinces_and_capital_cities)

if __name__ == "__main__":
    main()
