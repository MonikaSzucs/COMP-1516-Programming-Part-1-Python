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

    this_dict = {
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

    utilities_dict.display_all(this_dict)
    print(utilities_dict.get_capital_city("British Columbia", this_dict))

    utilities_dict.add_element("New_Province", "New_Capital_City", this_dict)
    utilities_dict.remove_item("New_Province", this_dict)

    canada = {
        "ontario": {"capital": "toronto", "largest": "toronto", "population": "14826276"},
        "quebec": {"capital": "quebec city", "largest": "montreal", "population": "8604495"},
        "nova scotia": {"capital": "halifax", "largest": "halifax", "population": "992055"},
        "new brunswick": {"capital": "fredericton", "largest": "moncton", "population": "789225"},
        "manitoba": {"capital": "winnipeg", "largest": "winnipeg", "population": "1383765"},
        "british columbia": {"capital": "victoria", "largest": "vancouver", "population": "5214805"},
        "prince edward island": {"capital": "charlottetown", "largest": "charlottetown", "population": "164318"},
        "saskatchewan": {"capital": "regina", "largest": "saskatoon", "population": "1179844"},
        "alberta": {"capital": "edmonton", "largest": "calgary", "population": "4442879"},
        "newfoundland and labrador": {"capital": "st. john's", "largest": "st. john's", "population": "520553"}
    }
    print(utilities_dict.get_total_population(canada))
    print(utilities_dict.get_another_capital_city("Quebec", canada))
    print(utilities_dict.get_another_capital_city("Display None", this_dict))
    print(utilities_dict.get_largest_city("Quebec", canada))
    print(utilities_dict.get_largest_city("Display None", canada))
    print(utilities_dict.get_smallest_province(canada))
    print(utilities_dict.get_largest_province(canada))
    print(utilities_dict.get_province_description("Alberta", canada))
    print(utilities_dict.get_province_description("ontario", canada))
    print(utilities_dict.get_province_description("Display None", canada))


if __name__ == "__main__":
    main()
