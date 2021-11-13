"""
Assignment 2 by Monika Szucs A00878763
A script containing the main() working function
:author: Monika Szucs
:date: November 13, 2021
"""

# importing tuple, functions and regex
from assignment2 import write_countries_capitals_to_file, save_capitals
import re
from data import countries_and_capitals, countries, capitals


def main():
    file_name = input("Please enter a file name: ")
    write_countries_capitals_to_file(file_name)
    save_capitals("vowel_vowel_vowel.txt")
    save_capitals("cons_cons_cons.txt")
    save_capitals("i_before_e.txt")
    save_capitals("a_a.txt")
    save_capitals("end_with_vowel.txt")
    save_capitals("weird.txt")
    save_capitals("not_start.txt")


if __name__ == '__main__':
    main()


