"""
Lab 8 by Monika Szucs A00878763
A script containing the get_countries(substring), get_capitals(substring), get_file_data()
:author: Monika Szucs
:date: November 7, 2021
"""

# importing the tuples from the data file
from data import countries, capitals


def get_countries(substring):
    """
        A function that will loop through the countries tuple. Grab the substring paramater in the country tuple,
        create a brand-new file named "lab-week-8.txt" for writing and write that country name on its own line in
        the file. Then close the file.
        First Variant and parameter
        :param substring: contains a substring parameter entered in by the user.
    """
    file_script = open("lab-week-8.txt", "w")
    initial = 0
    for country in countries:
        if substring.lower() in country.lower() and initial == 0:
            file_script.write(country)
            initial += 1
        elif substring.lower() in country.lower():
            file_script.write("\n" + country)
    file_script.close()


def get_capitals(substring):
    """
        A function that will re-open the "lab-week-8.txt" file for appending, loop through the capitals tuple. If a
        capital contains the substring parameter, append that capital to the end of the file, on its own line.
        Then close the file.
        Second Variant and parameter
        :param substring: contains a substring parameter entered in by the user.
    """
    file_script = open("lab-week-8.txt", "a")
    for capital in capitals:
        if substring.lower() in capital.lower():
            file_script.write("\n" + capital)
    file_script.close()


def get_file_data():
    """
        A function that will re-open the "lab-week-8.txt" file for reading. Use the readlines() function to loop
        through the file and display each of the lines to the screen.
        Third Variant
    """
    file_script = open("lab-week-8.txt", "r")
    current_line = file_script.readlines()
    for item in current_line:
        print(item.strip())
    file_script.close()
