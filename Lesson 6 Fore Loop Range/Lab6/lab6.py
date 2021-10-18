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
    while True:
        try:
            first_number, second_number, divisor = map(int, input
            ("enter in two numbers and a divisor (The divisor cannot be zero): ").split())
        except ValueError as e:
            print(e)
            first_number, second_number, divisor = map(int, input
            ("enter in two numbers and a divisor with spaces inbetween: ").split())


    print(first_number)
    print(second_number)
    print(divisor)


def main():
    weight_converter()
    get_divisible()


if __name__ == "__main__":
    main()
