"""
Assignment 1 by Monika Szucs A00878763
A script containing the original main() function
:author: Monika Szucs
:date: October 25, 2021
"""

import utilities_sets


def main():
    set1 = {"apple", "banana", "orange", "peach"}
    set2 = {"banana", "pineapple", "peach", "watermelon"}
    print(utilities_sets.get_total_items(set1))
    print()
    utilities_sets.display_all_items(set1)
    set1 = utilities_sets.add_item(set1, "cantaloupe")
    print()
    utilities_sets.display_all_items(set1)


if __name__ == "__main__":
    main()
