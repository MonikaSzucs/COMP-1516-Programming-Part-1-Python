"""
A script to run the is_magic_date() function and checks the month, day then year value then checks
to see if the day and month multiplied together equals the two digit year which is the magic number
It will just printer out a statement saying if it is a magic number or not.
:author: Monika Szucs
:date: October 3 2021
"""
def is_magic_date():
    """
    a function that will ask the user for a month value, day value and year value. It will check all values match exact
    requirements. If not it will display an error. If it passes then the final step will be to check
    if the day value multiplied by the month value equals the two digit year value. If so then it
    is a magic number.
    Third Variant
    """
    print(" running is magic date:")
    month_value = int(input("input month value:", ))

    if 1 <= month_value <= 12:
        day_value = int(input("input day value:", ))
        if 1 <= day_value <= 31:
            two_digit_year_value = int(input("input two digit year value:", ))
            if 10 <= two_digit_year_value <= 99:
                two_digit = day_value*month_value
                if two_digit == two_digit_year_value:
                    print("the date ", day_value, "-", month_value, "-", two_digit, "is a magic date")
                else:
                    print("the date ", day_value, "-", month_value, "-", two_digit, "is not a magic date")

            else:
                print("the year value must be positive and it must be two digits")
        else:
            print("invalid day value")
    else:
        print("invalid month value")

