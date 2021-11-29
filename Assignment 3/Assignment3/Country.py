"""
Assignment 3 by Monika Szucs A00878763
A script containing the main() function that should not be called, the class Country with functions __init__,
print_details, birth, death, and disaster
:author: Monika Szucs
:date: November 28, 2021
"""


class Country:
    """ Represents a car in a car lot """

    def __init__(self, country_name, capital_name, population):
        """ Initializes the Country details """
        """
            A constructor that initializes the object
            First Variant and parameters
            :param self: set up OOP to call values later within each function
            :param country_name: Contains a country name
            :param capital_name: contains a capital name
            :param population: Contains a population for the country/capital
        """

        try:
            self._country_name = country_name
            self._capital_name = capital_name
            if population < 2000000:
                raise ValueError("Population " + str(population) + " is too low")
            else:
                self._population = population
        except ValueError as e:
            print(str(e))

    def print_details(self):
        """ Returns the projected details """
        """
            A function that will return the projected details of the Country
            Second Variant, parameter, and return
            :param self: will use the self items from the __init__ constructor 
            :return: a sentence with the country, population, and capital
        """
        try:
            return "The capital of " + self._country_name + " (pop. " + str(
                self._population) + ") is " + self._capital_name.upper()
        except AttributeError as a:
            print("There is an error with your input")

    def birth(self):
        """
            A function that will grab the population detail of the Country and add one to the population
            Third Variant, parameter, and return
            :param self: will grab a value from the constructor
            :return: the updated population for the country
        """
        birth_population = self._population + 1
        return birth_population

    def death(self, reduction):
        """
            A function that will grab the details of the car and then calculate the profit minus the reduction
            to return the reduced price
            Fourth Variant, parameters, and return
            :param self: allows the calling of the constructor
            :param reduction: contain the amount (1) by which the population will decrease
            :return: the reduced population by 1
        """
        reduced_price = self._population - reduction
        return reduced_price

    def disaster(self, reduction):
        """
            A function that will remove 100 million from a population that is above 100 million or make the population
            set to 0 if it is below 100 million
            Fourth Variant, parameters, and return
            :param self: allows the calling of the constructor
            :param reduction: contains a reduced amount (100 million) from a disaster
            :return: the reduced population based on a disaster
        """
        population = self._population
        if population >= reduction:
            population = population - reduction
            return population
        else:
            population = 0
            return population


def main():
    print("I should not be called")


if __name__ == "__main__":
    main()
