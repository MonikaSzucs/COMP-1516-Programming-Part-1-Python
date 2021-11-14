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
        print(type(self._price))
        return "%s %s %s for sale for $%.2f" % (self._year, self._make, self._model, float(self._price))

    def reduce_price(self, reduction):
        # TODO
        reduced_price = self.calc_profit() - reduction
        return reduced_price

