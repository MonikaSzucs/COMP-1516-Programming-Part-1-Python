from math import sqrt
from itertools import count, islice


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
    normal_hours = 40
    for i in range(number_of_employees):
        list_of_list.append([])
        # In each iteration, add an empty list to the main list
        try:
            worked_hours = input("Please enter the number of worked hours: ")
            if type(int(worked_hours)) == int:
                list_of_list[i].append(int(worked_hours))
                continue
        except (TypeError, NameError, ValueError):
            print("Please only enter in positive numbers")
    for i in range(number_of_employees):
        if 0 <= list_of_list[i][0] <= int(normal_hours):
            total = int(list_of_list[i][0]) * hourly_rate
            list_of_list[i].append(total)
            print("the employee worked for " + str(int(list_of_list[i][0])) + " hours and earned " + str("{:.2f}".format(list_of_list[i][1])) + " $")
        elif list_of_list[i][0] > normal_hours:
            overtime = int(list_of_list[i][0]) - normal_hours
            total = int(overtime * hourly_rate * 1.5) + (normal_hours * hourly_rate)
            list_of_list[i].append(total)
            print("the employee worked for " + str(int(list_of_list[i][0])) + " hours and earned " + str("{:.2f}".format(list_of_list[i][1])) + " $")


def is_prime(is_value):
    return is_value > 1 and all(is_value % i for i in islice(count(2), int(sqrt(is_value) - 1)))


def get_prime_numbers(is_number):
    is_list = []
    i = 2
    while i <= is_number:
        is_list.append(i)
        i += 1
    return is_list


def main():
    weight_converter()
    get_divisible()
    get_list_stats()

    try:
        number_of_employees, hourly_rate = [int(x) for x in input("Enter in the number of employees and the hourly rate: ").split()]
        print("Number of Employees is: ", number_of_employees)
        print("The Hourly Rate is: ", hourly_rate)
        calculate_pay(number_of_employees, hourly_rate)
    except ValueError:
        print("Make sure you only type in two numbers")

    while True:
        prime_value = int(input("Please enter a value that is great than 2: "))
        if prime_value > 2:
            numbers_returned = get_prime_numbers(prime_value)
            break
    print(numbers_returned)
    for number in numbers_returned:
        if is_prime(number):
            print("the number " + str(number) + " is prime number")

if __name__ == "__main__":
    main()
