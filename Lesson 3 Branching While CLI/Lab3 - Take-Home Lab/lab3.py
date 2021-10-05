"""
A script to run the functions is_even(), get_pocket_color(), and play_roulette() which will be used to play
the roulette wheel.
The is_even() function will return True or False
The get_pocket_color() function will return pockets, color , and boolean_value
The play_roulette() function will grab the values from is_even() and get_pocket_color() and then check
to see how much the user will win based on their bet amount.
:author: Monika Szucs
:date: October 4 2021
"""


def is_even(pockets):
    """
    a function to return if the value is even or odd using the values True or False
    Third variant, paramters, and return
    :param pockets: grabs a the value the user entered which is between 0 and 36 inclusive
    :return: True if even or False is Odd
    """
    if (pockets % 2) == 0:
        return True
    else:
        return False


def get_pocket_color():
    """
    a function asks the user for a value between 0 and 36 inclusive. Then calls the is_even() function
    to check if it is True or False. Then checked to see what range the number entered in by the user is.
    If it is between 0 and 36 then it will proceed and if not it will display an error message.
    If the pocket number is equal to 0 then it will return the pocket value and the color green
    If the pocket number is between 1 and 10 inclusive then it will check if it is an even or odd number
    If the pocket number is between 11 and 18 inclusive it will check if it is an even or odd number
    If the pocket number is between 19 and 28 inclusive it will check if it is an even or odd number.
    If the pocket number is between 19 and 36 inclusive it will check if it is an even or odd number.
    Second variant and return
    :return: pockets, color, and boolean_value
    """
    while True:
        try:
            pockets = int(input("Please enter a number between 0 to 36 inclusive: "))
            boolean_value = is_even(pockets)
            if 0 <= pockets <= 36:
                if pockets == 0:
                    return pockets, "green"
                if 1 <= pockets <= 10:
                    if boolean_value:
                        return pockets, "black", boolean_value
                    else:
                        return pockets, "red", boolean_value
                elif 11 <= pockets <= 18:
                    if boolean_value:
                        return pockets, "red", boolean_value
                    else:
                        return pockets, "black", boolean_value
                elif 19 <= pockets <= 28:
                    if boolean_value:
                        return pockets, "black", boolean_value
                    else:
                        return pockets, "red", boolean_value
                elif 29 <= pockets <= 36:
                    if boolean_value:
                        return pockets, "red", boolean_value
                    else:
                        return pockets, "black", boolean_value
            else:
                print("You have not listened to instructions. Please enter a number only between 0 and 36 inclusive: ")
        except:
            print("You have not entered a number between 0 and 36 inclusive. Please try again: ")


def play_roulette():
    """
    a function that runs the function get_pocket_color() and returns values.
    Then we grab the bet amount from the user.
    We then check the pocket number returned from get_pocket_color() and the color to see if the player
    won or lost the bet
    First variant and parameters
    """
    integer_color = get_pocket_color()
    integer_number = int(integer_color[0])
    color = integer_color[1]
    boolean_value = integer_color[2]
    print(integer_number)
    print(color)
    print(boolean_value)
    bet_amount = input("enter your bet amount")

    if integer_number == 0 and color == "green":
        print(" you neither win nor lose you have %s $" % float(bet_amount))
    elif boolean_value and color == "black":
        bet_amount = float(bet_amount) * 1.50
    elif not boolean_value and color == "black":
        bet_amount = 0
    elif boolean_value and color == "red":
        bet_amount = float(bet_amount) * 2.00
    elif not boolean_value and color == "red":
        bet_amount = float(bet_amount) * 1.50

    if int(bet_amount) > 0:
        print("you won you have %s $" % bet_amount)
    elif int(bet_amount) == 0:
        print("You have not won any money")
    else:
        print("You owe money! Pay up!")


def main():
    print("running play roulette")
    """ 
    This is a loop that will keep running until the player types in something other than the word "yes"
    In the while loop the play_roulette() function will keep being called unless the user wants to break out of the game
    """
    while True:
        play_roulette()
        play_again = input("Do you want to play again? type \"yes\" to continue, anything else to stop: ")
        if play_again == "yes":
            continue
        else:
            break


if __name__ == "__main__":
    main()
