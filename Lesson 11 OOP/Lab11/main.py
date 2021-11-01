from car import Car


def main():
	car1 = Car("Honda", "Civic", 2020, 15000.0, 20000)
	print(car1.get_details())
	print("First Car’s Initial Profit is $%.2f" % car1.calc_profit())
	car1.reduce_price(1000)
	print("First Car’s New Profit is $%.2f" % car1.calc_profit())

	car2 = Car("BMW", "M3", 2019, 30000, 50000)
	print(car2.get_details())
	print("First Car’s Initial Profit is $%.2f" % car2.calc_profit())
	car2.reduce_price(5000.50)
	print("First Car’s New Profit is $%.2f" % car2.calc_profit())


if __name__ == '__main__':
	main()