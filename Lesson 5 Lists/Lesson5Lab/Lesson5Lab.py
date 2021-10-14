"""
A script with three tuples and the main function
:author: Monika Szucs
:date: October 13 2021
"""
import information as info


def main():
    print(info.how_many_countries())
    print(info.get_name_of_longest_country())
    print(info.get_number_of_capitals_containing("e"))
    print(info.get_number_of_capitals_containing("z"))
    print(info.get_number_of_capitals_containing("'"))
    print(info.get_number_of_capitals_containing("an"))
    print(info.get_countries_and_capitals_that_start_with_same_letter())
    print(info.get_capital_of('canada'))
    print(info.get_capital_of('nEW zeALAND'))
    print(info.get_capital_of('xyz'))
    print(info.get_list_of_countries_with_this_many_letters_in_name(11))
    print(info.get_list_of_countries_with_this_many_letters_in_name(15))
    print(info.get_capitals_and_countries_that_begin_and_end_with_same_letter())
    print(info.print_countries_in_reverse_alphabetical_order())


if __name__ == "__main__":
    main()

