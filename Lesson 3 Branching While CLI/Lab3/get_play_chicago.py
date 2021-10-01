import random


def play_chicago():
    print(" running play chicago")
    rounds = 11
    round_number = 2
    end = round_number + rounds
    points = 0
    game_on = True

    while round_number < end:

        if game_on == True:
            print("round number", round_number)
            number_one = random.randint(1, 6)
            number_two = random.randint(1, 6)
            print("first dice number ", number_one)
            print("second dice number ", number_two)
            total_number = number_one + number_two
            if total_number == round_number:
                points += 1
                print("You won a point, your current points are: ", points)

            else:
                print("No points, your current points are ", points)
            round_number += 1

        answer = input("do you want to play again?, enter \"yes\" to continue ")

        if answer == "yes":
            pass
        elif answer == "no":
            break

    print("the game is over you earned ", points, " points")
