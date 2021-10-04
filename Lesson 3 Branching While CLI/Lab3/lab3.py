"""
A script with the main function used to call all the other functions
:author: Monika Szucs
:date: October 3 2021
"""

# import all modules to get loan qualifier, magic date, and play chicago
import get_loan_qualifier
import get_magic_date
import get_play_chicago


def main():
    get_loan_qualifier.loan_qualifier()
    get_magic_date.is_magic_date()
    get_play_chicago.play_chicago()


if __name__ == "__main__":
    main()
