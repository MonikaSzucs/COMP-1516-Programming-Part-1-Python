class Car:
    """ Represents a car in a car lot """

    def __init__(self, make, model, year, cost, price):
        """ Initializes the car details """
        self._make = make
        self._model = model
        self._year = year
        self._cost = cost
        self._price = price

    def calc_profit(self):
        """ Returns the projected profit """
        return self._price - self._cost

    def get_details(self):
        # TODO
        return "%s %s %s for sale for %s" % (self._year, self._make, self._model, self._price)

    def reduce_price(self, reduction):
        # TODO
        pass

