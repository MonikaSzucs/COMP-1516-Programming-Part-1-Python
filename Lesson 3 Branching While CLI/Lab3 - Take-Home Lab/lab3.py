def is_even(integer_number):
    if (integer_number % 2) == 0:
        return True
    else:
        return False


def get_pocket_color():
    while True:
        try:
            pockets = int(input("Please enter a number between 0 to 36"))
            if 0 <= pockets <= 36:
                if 0 == pockets:
                    return pockets, "green"
                if 1 <= pockets <= 10:
                    if (pockets % 2) == 0:
                        return pockets, "black"
                    else:
                        return pockets, "red"
                elif 11 <= pockets <= 18:
                    if (pockets % 2) == 0:
                        return pockets, "red"
                    else:
                        return pockets, "black"
                elif 19 <= pockets <= 28:
                    if (pockets % 2) == 0:
                        return pockets, "black"
                    else:
                        return pockets, "red"
                elif 29 <= pockets <= 36:
                    if (pockets % 2) == 0:
                        return pockets, "red"
                    else:
                        return pockets, "black"
            else:
                print("You have not listened to instructions. Please enter a number only between 0 and 36 inclusive: ")
        except:
            print("You have not entered a number between 0 and 36 inclusive. Please try again: ")


def play_roulette():
    print("running play roulette")
    integer_color = get_pocket_color()
    integer_number = int(integer_color[0])
    color = integer_color[1]

    print(integer_number)
    print(color)

    bet_amount = input("enter your bet amount")

    boolean_value = is_even(integer_number)
    print(bet_amount)
    print(boolean_value)
    round_number = 0

    if integer_number == 0 and color == "green":
        print(" you neither win nor lose you have %s $" % float(bet_amount))
    elif integer_number and color == "black":
        bet_amount = float(bet_amount * 1.50)
    elif integer_number and color == "red":
        bet_amount = float(bet_amount * 2.00)
    elif integer_number is False and color == "black":
        bet_amount = float(bet_amount * 0.5)

    if int(bet_amount) > 0:
        print(bet_amount)
    elif int(bet_amount) == 0:
        print("You have not won any money")
    else:
        print("You owe money! Pay up!")


def main():
    while True:
        play_roulette()
        play_again = input("Do you want to play again? type \"yes\" to continue, anything else to stop: ")
        if play_again == "yes":
            continue
        else:
            break


if __name__ == "__main__":
    main()
