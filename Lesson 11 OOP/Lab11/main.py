"""
Lab 11 by Monika Szucs A00878763
A script containing the main() working function
:author: Monika Szucs
:date: November 13, 2021
"""

# importing the file Car and its functions with OOP
from car import Car


def main():
	car0 = Car("Honda", "Civic", 2015, 15000.0, 9999.99)
	print(car0.get_details())
	print()

	car1 = Car("Honda", "Civic", 2020, 15000.0, 20000)
	print(car1.get_details())
	print("First Car’s Initial Profit is $%.2f" % car1.calc_profit())
	print("First Car’s New Profit is $%.2f" % car1.reduce_price(1000))
	print()

	car2 = Car("BMW", "M3", 2019, 30000, 50000)
	print(car2.get_details())
	print("Second Car’s Initial Profit is $%.2f" % car2.calc_profit())
	print("Second Car’s New Profit is $%.2f" % car2.reduce_price(5000.50))


if __name__ == '__main__':
	main()
