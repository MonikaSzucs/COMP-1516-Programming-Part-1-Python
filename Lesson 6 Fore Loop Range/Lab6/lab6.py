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
    list_stats = []
    while True:
        try:
            positive_integer = input("Please enter a positive integer: ")
            if type(int(positive_integer)) == int:
                print("it is a integer")
                if int(positive_integer) >= 0:
                    list_stats.append(int(positive_integer))
                else:
                    continue
        except (TypeError, NameError, ValueError):
            print("Please only enter in a positive integer (greater than 0)")
            if positive_integer.isspace():
                print("There is a space it must end")
                break
    print(list_stats)
    print("The length of the list is: " + str(len(list_stats)))
    even_count = 0
    for num in list_stats:
        if num % 2 == 0:
            even_count += 1
    print("The number of even numbers are: " + str(even_count))

    list_stats.sort()
    print("The min number is: " + str(list_stats[0]))
    print("The max number is: " + str(list_stats[-1]))


def calculate_pay(number_of_employees, hourly_rate):
    list_of_list = []
    print("inside function")
    print(number_of_employees)
    print(hourly_rate)
    normal_hours = 40
    for i in range(number_of_employees):
        list_of_list.append([])
        print(i)
        # In each iteration, add an empty list to the main list
        try:
            worked_hours = input("Please enter the number of worked hours: ")
            if type(int(worked_hours)) == int:
                print(worked_hours)
                list_of_list[i].append(int(worked_hours))
                print(list_of_list)
                continue
        except (TypeError, NameError, ValueError):
            print("Please only enter in positive numbers")
    print(worked_hours)
    print("NORMAL HOURS:")
    print(normal_hours)
    print("second if and else statement")
    for i in range(number_of_employees):
        print("VALUE CHECK")
        print(int(worked_hours))
        print(int(normal_hours))
        print(list_of_list[i][0])
        if 0 <= list_of_list[i][0] <= int(normal_hours):
            print("less than 40")
            total = int(list_of_list[i][0]) * hourly_rate
            list_of_list[i].append(total)
            print("values:")
            print(list_of_list)
        elif list_of_list[i][0] > normal_hours:
            print("greater than 40")
            overtime = normal_hours - int(worked_hours)
            print(overtime)
            total = int(overtime * hourly_rate * 1.5) + (normal_hours * hourly_rate)
            print(total)
            list_of_list[i].append(total)
            print(list_of_list)


def prime():
    pass


def get_prime_numbers():
    pass


def main():
    # weight_converter()
    # get_divisible()
    # get_list_stats()
    try:
        number_of_employees, hourly_rate = [int(x) for x in input("Enter in the number of employees and the hourly rate: ").split()]
        print("Number of Employees is: ", number_of_employees)
        print("The Hourly Rate is: ", hourly_rate)
        calculate_pay(number_of_employees, hourly_rate)
    except ValueError:
        print("Make sure you only type in two numbers")

    get_prime_numbers()


if __name__ == "__main__":
    main()
