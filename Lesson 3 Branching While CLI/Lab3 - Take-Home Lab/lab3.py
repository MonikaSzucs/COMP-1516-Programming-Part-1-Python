def is_even(integer_number):
    if (integer_number % 2) == 0:
        return True
    else:
        return False


def get_pocket_color():
    pockets = int(input("Please enter a number between 0 to 36"))
    if 0 <= pockets <= 36:
        if 0 == pockets:
            return "green"
        if 1 <= pockets <= 10:
            if (pockets % 2) == 0:
                return "black"
            else:
                return "red"
        elif 11 <= pockets <= 18:
            if (pockets % 2) == 0:
                return "red"
            else:
                return "black"
        elif 19 <= pockets <= 28:
            if (pockets % 2) == 0:
                return "black"
            else:
                return "red"
        elif 29 <= pockets <= 36:
            if (pockets % 2) == 0:
                return "red"
            else:
                return "black"
    else:
        print("Please enter a number")


def play_roulette(integer_number, integer_number_returned, colors):
    pocket_number = input("enter a pocket number between 0 and 36 inclusive: ")
    bet_amount = input("enter your bet amount")
    round_number = 0
    while round_number <= integer_number:
        
        if integer_number == 0 and colors == "green":
            print(" you neither win nor lose you have ", bet_amount, " $")
        elif integer_number_returned and colors == "black":
            bet_amount = bet_amount * 1.50
        elif integer_number_returned and colors == "red":
            bet_amount = bet_amount * 2.00
        elif integer_number_returned is False and colors == "black":
            bet_amount = bet_amount * 0.5
    print(bet_amount)


def main():
    integer_number = int(input("Please enter a number: ", ))
    integer_number_returned = is_even(integer_number)
    print(integer_number_returned)
    colors = get_pocket_color()
    print(colors)
    play_roulette(integer_number, integer_number_returned, colors)


if __name__ == "__main__":
    main()
