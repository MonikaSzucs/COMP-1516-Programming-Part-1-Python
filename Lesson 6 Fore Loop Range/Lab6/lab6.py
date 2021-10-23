def weight_converter():
    kilogram_base = 1
    pounds_base = 2.20
    kilogram = 30
    while True:
        if kilogram <= 100:
            floating_number = kilogram * pounds_base
            print("weight in Kilos:   %d  is   %.2f in Pounds" % (kilogram, floating_number))
        else:
            break
        kilogram += 10


def get_divisible():
    check = 0
    while True:
        try:
            if check == 0:
                first_number, second_number, divisor = map(int, input
                ("enter in two numbers and a divisor (The divisor cannot be zero): ").split())
            elif check == 1:
                first_number, second_number, divisor = map(int, input
                ("Make sure you only enter in whoel digits. "
                 "Enter in two numbers and a divisor (The divisor cannot be zero): ").split())
            if divisor > first_number and divisor > second_number:
                print("The third number (divisor) cannot be bigger than the first or second number")
                continue
            if divisor == 0:
                print("the divisor cannot be 0")
                break
            elif first_number <= second_number:
                print("first number less than second")
                for x in range(first_number, second_number + 1):
                    if x % divisor == 0:
                        print(x)
                break
            elif first_number > second_number:
                print("first number greater than second")
                for y in range(first_number - 1, second_number + 1, -1):
                    if y % divisor == 0:
                        print(y)
                break
        except ValueError as e:
            print(e)
            pass


def get_list_stats():
    positive_integer = input("Please enter a positive integer: ")



def main():
    weight_converter()
    get_divisible()


if __name__ == "__main__":
    main()
