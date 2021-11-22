"""
Assignment 3 by Monika Szucs A00878763
A script containing the main() function
:author: Monika Szucs
:date: November 23, 2021
"""

class Country:
    """ Represents a car in a car lot """
    def __init__(self, country_name, capital_name, population):
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
        self._country_name = country_name
        self._capital_name = capital_name
        self._population = population

    def print_details(self):
        """ Returns the projected profit """
        """
            A function that will return the projected profit
            Second Variant, parameter, and return
            :param self: contains all the values of the car entered in by the user 
            :return: the projected profit of the car
        """
        return self._country_name - self._capital_name

    def birth(self):
        """
            A function that will grab the details of the car and present it in a nicely formatted sentence
            Third Variant, parameter, and return
            :param self: contains all the values of the car entered in by the user
            :return: the details of the car in a formatted sentence
        """
        birth_population = self._population() + 1
        return birth_population

    def death(self, reduction):
        """
            A function that will grab the details of the car and then calculate the profit minus the reduction
            to return the reduced price
            Fourth Variant, parameters, and return
            :param self: contains all the values of the car entered in by the user
            :param reduction: contains the reduced amount
            :return: the reduced price
        """
        reduced_price = self._population() - 1
        return reduced_price

    def disaster(self, reduction):
        """
            A function that will grab the details of the car and then calculate the profit minus the reduction
            to return the reduced price
            Fourth Variant, parameters, and return
            :param self: contains all the values of the car entered in by the user
            :param reduction: contains the reduced amount
            :return: the reduced price
        """
        population = self._population
        subtract_population = 100000000
        if population > subtract_population:
            population = population - subtract_population
            return population
        else:
            population = 0
            return population


def main():
    pass


if __name__ == "__main__":
    main()

