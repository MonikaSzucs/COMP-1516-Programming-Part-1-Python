"""
Assignment 1 by Monika Szucs A00878763
A script containing the original main() function
:author: Monika Szucs
:date: October 25, 2021
"""
import assignment1


def main():
    assignment1.print_json_countries_and_capitals()
    print(assignment1.get_list_of_countries_whose_nth_letter_is(3,"m"))
    print(assignment1.get_funny_case_capital_cities("u"))
    print(assignment1.get_funny_case_capital_cities("z"))
    print(assignment1.get_funny_case_capital_cities("w"))
    #print(assignment1.get_doubled_letter_countries())


if __name__ == "__main__":
    main()

