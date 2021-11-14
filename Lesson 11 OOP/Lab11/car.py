"""
Lab 11 by Monika Szucs A00878763
A script containing the class Car with def __init__, calc_profit(), get_details(), reduce_price()
:author: Monika Szucs
:date: November 13, 2021
"""

class Car:
    """ Represents a car in a car lot """
    def __init__(self, make, model, year, cost, price):
        """ Initializes the car details """
        """
            A function that will grab the values entered in by the user and organize it into its self container to be 
            used later
            First Variant and parameters
            :param self: set up OOP to call values later within each function
            :param make: Contains the make of the car
            :param model: Contains the Model name of the car
            :param year: Contains the year of when the car was built
            :param cost: Contains the cost of the car
            :param price: Contains the initial price of the car
        """
        self._make = make
        self._model = model
        self._year = year
        self._cost = cost
        self._price = price

    def calc_profit(self):
        """ Returns the projected profit """
        """
            A function that will return the projected profit
            Second Variant, parameter, and return
            :param self: contains all the values of the car entered in by the user 
            :return: the projected profit of the car
        """
        return self._price - self._cost

    def get_details(self):
        """
            A function that will grab the details of the car and present it in a nicely formatted sentence
            Third Variant, parameter, and return
            :param self: contains all the values of the car entered in by the user
            :return: the details of the car in a formatted sentence
        """
        print(type(self._price))
        return "%s %s %s for sale for $%.2f" % (self._year, self._make, self._model, float(self._price))

    def reduce_price(self, reduction):
        """
            A function that will grab the details of the car and then calculate the profit minus the reduction
            to return the reduced price
            Fourth Variant, parameters, and return
            :param self: contains all the values of the car entered in by the user
            :param reduction: contains the reduced amount
            :return: the reduced price
        """
        reduced_price = self.calc_profit() - reduction
        return reduced_price

