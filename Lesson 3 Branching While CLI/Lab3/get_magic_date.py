def is_magic_date():
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

