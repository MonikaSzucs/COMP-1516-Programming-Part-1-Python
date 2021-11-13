"""
Assignment 2 by Monika Szucs A00878763
A script containing the write_countries_capitals_to_file(), save_capitals(file), and not working main() Function
:author: Monika Szucs
:date: November 13, 2021
"""

# importing tuple, functions and regex
from data import countries_and_capitals, countries, capitals, countries_capitals_dictionary
import re


def write_countries_capitals_to_file(file):
    """
        A function that will take in a file parameter and then check to make sure it fits the desired requirements which
        is must contains only letters or digits and must be between 1-8 characters in length plus .txt extension
        First Variant and parameter
        :param file: contains the file name entered in by the user
    """
    print(type(file))
    while True:
        if re.search(r"^[a-zA-Z0-9]{1,8}.txt$", file):
            file_script = open(file, "w")
            position = 0
            for country, capital in countries_capitals_dictionary.items():
                if position == 0:
                    file_script.write("The capital of %s is %s." % (country, capital))
                    position += 1
                else:
                    file_script.write("\nThe capital of %s is %s." % (country, capital))
            file_script.close()
            break
        else:
            file = input("Must be of length 1-8 characters, plus a “.txt” file extension. Please enter a file name: ")


def save_capitals(file):
    """
        A function that will first check:
        1. To see if the Capital contains three consecutive vowels with the file name vowel_vowel_vowel.txt
        2. To see if the Capital contains three consecutive consonants file named cons_cons_cons.txt
        3. To see if the Capital contains i somewhere before e and file named i_before_e.txt
        4. To see if the Capital starts with a and ends with a and file named a_a.txt
        5. To see if the Capital ends with a vowel and file named end_with_vowel.txt
        6. To see if the Capital contains apostrophe, space or x and file named weird.txt
        7. To see if the Capital does not start with a-e, l-p, or s and file named not_start.txt
        Second Variant and parameter
        :param file: has a file parameter which then gets checked to see what should be saved in a .txt file
    """
    print("CHECKING save capitals")
    print(file)
    file_created = open(file, "w")
    position = 0
    print()
    for capital_found in capitals:
        if (re.search(r"[aeiouAEIOU]{3}", capital_found)) and file == "vowel_vowel_vowel.txt":
            print(capital_found)
            if position == 0:
                file_created.write(capital_found.lower())
                position += 1
            else:
                file_created.write("\n" + capital_found.lower())
        elif (re.search(r"[b-dB-Df-hF-Hj-nJ-Np-tP-Tv-zV-Z]{3}", capital_found)) and file == "cons_cons_cons.txt":
            print(capital_found)
            if position == 0:
                file_created.write(capital_found.lower())
                position += 1
            else:
                file_created.write("\n" + capital_found.lower())
        elif (re.search("i.+e|i+e", capital_found)) and file == "i_before_e.txt":
            print(capital_found)
            if position == 0:
                file_created.write(capital_found.lower())
                position += 1
            else:
                file_created.write("\n" + capital_found.lower())
        elif (re.search("^[aA]", capital_found)) and file == "a_a.txt":
            capital_lowered = capital_found.lower()
            if re.search("[aA]$", capital_lowered):
                print(capital_found)
                if position == 0:
                    file_created.write(capital_lowered)
                    position += 1
                else:
                    file_created.write("\n" + capital_lowered)
        elif (re.search("[aAeEiIoOuUyY]$", capital_found)) and file == "end_with_vowel.txt":
            print(capital_found)
            if position == 0:
                file_created.write(capital_found.lower())
                position += 1
            else:
                file_created.write("\n" + capital_found.lower())
        elif (re.search("['\sx]", capital_found)) and file == "weird.txt":
            print(capital_found)
            if position == 0:
                file_created.write(capital_found.lower())
                position += 1
            else:
                file_created.write("\n" + capital_found.lower())
        elif (re.search("^[^a-eA-El-pL-PsS]", capital_found)) and file == "not_start.txt":
            print(capital_found)
            if position == 0:
                file_created.write(capital_found.lower())
                position += 1
            else:
                file_created.write("\n" + capital_found.lower())
    file_created.close()
    print()


def main():
    print("I should not be called")


if __name__ == '__main__':
    main()
