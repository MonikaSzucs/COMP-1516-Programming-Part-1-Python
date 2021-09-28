print(" running is magic date:")
month_value = input("input month value:",)
day_value = input("input day value:",)
two_digit_year_value = input("input two digit year value:",)


if month_value <= 12 && month_value >= 1:
    if day_value <= 31 && day_value >= 1:
        if two_digit_year_value >= 10 && two_digit_year_value <= 99:
            pass
        else:
            print("the year value must be positive and it must be two digits")
    else:
        print("the day value must be between 1 and 31 inclusive")
        pass
else:
    print("invalid month value")
    pass
