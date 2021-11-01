import locale


def display_all(this_dict):
    """
        A function that will display all of the Keys and Values of the given this_dict in a sample one sentence format
        "x is the capital city of y"
        First Variant, parameter
        :param this_dict: contains a dictionary of Canadian provinces and capital cities
    """
    print()
    print(this_dict)
    for place in this_dict:
        print("%s is the capital city of %s" % (this_dict[place], place))


def get_capital_city(province_name, this_dict):
    """
        A function that will return the capital city for the given province_name in the given this_dict
        Second Variant, parameters, return
        :param province_name: contains the province name
        :param this_dict: contains a dictionary of Canadian provinces and capital cities
        :return: the capital city of the given province_name
    """
    print()
    print("Returns the capital city for the given province name in the given dictionary")
    matching_province_name = ""
    for place in this_dict:
        if place == province_name:
            matching_province_name = this_dict[place]
    return matching_province_name


def add_element(province_name, capital_city, this_dict):
    """
        A function that adds a given key-value
        Third Variant and parameters
        :param province_name: contains the province name
        :param capital_city: contains the capital city of the province name
        :param this_dict: contains a dictionary of Canadian provinces and capital cities
    """
    print()
    print("Adds the given key-value")
    this_dict[province_name] = capital_city
    print(this_dict)


def remove_item(province_name, this_dict):
    """
        A function that will remove the given key from the dictionary
        Fourth Variant and parameters
        :param province_name: contains the province name
        :param this_dict: contains a dictionary of Canadian provinces and capital cities
    """
    print()
    print("Removes the given key from the dictionary")
    del this_dict[province_name]
    print(this_dict)


def get_total_population(this_dict):
    """
        A function that returns the total population of this_dict by summing up the population of each province
        Fifth Variant, parameter, return
        :param this_dict: contains a dictionary of Canadian provinces and capital cities
        :return: the total population within the dictionary
    """
    print()
    print("Returns the total population of this_dict by summing up the population of each province: ")
    population_number = 0
    for key in this_dict.keys():
        population_number += int(this_dict[key]["population"])
    locale.setlocale(locale.LC_ALL, 'en_US')
    return locale.format("%d", population_number, grouping=True)


def get_another_capital_city(province_name, this_dict):
    """
        A function that returns the name of the capital city for the given province_name.
        It will return None if the province_name doesn't exist
        Sixth Variant, parameter, return
        :param province_name: contains the province name
        :param this_dict: contains a dictionary of Canadian provinces and capital cities
        :return: the capital city for the given province_name
    """
    print()
    print("Returns the name of the capital city for the given province_name")
    retrieved_capital_city_name = "None"
    for key in this_dict.keys():
        if key == province_name.lower():
            retrieved_capital_city_name = this_dict[key]["capital"].title()
    return retrieved_capital_city_name


def get_largest_city(province_name, this_dict):
    """
        A function that returns the name of the largest city for the given province_name
        Seventh Variant, parameter, return
        :param province_name: contains the province name
        :param this_dict: contains a dictionary of Canadian provinces and capital cities
        :return: the name of the largest city for the given province_name
    """
    print()
    print("Returns the name of the largest city for the given province name")
    retrieved_largest_city = 'None'
    for key in this_dict.keys():
        if key == province_name.lower():
            retrieved_largest_city = this_dict[key]["largest"].title()
    return retrieved_largest_city


def get_smallest_province(this_dict):
    """
        A function that returns the name of the province with teh smallest population
        Eighth Variant, parameter, return
        :param this_dict: contains a dictionary of Canadian provinces and capital cities
        :return: the name of the province with the smallest population
    """
    print()
    print("Returns the name of the province with the smallest population")
    retrieved_smallest_population = 999999999
    smallest_province_population = ''
    for key in this_dict.keys():
        new_population = int(this_dict[key]["population"])
        if new_population < retrieved_smallest_population:
            retrieved_smallest_population = int(this_dict[key]["population"])
            smallest_province_population = key
    return smallest_province_population.title()


def get_largest_province(this_dict):
    """
        A function that returns the name of the province with the largest population
        Ninth Variant, parameter, return
        :param this_dict: contains a dictionary of Canadian provinces and capital cities
        :return: the the name of the province with the largest population
    """
    print()
    print("Returns the name of the province with the largest population")
    retrieved_smallest_population = 0
    smallest_province_name = ''
    for key in this_dict.keys():
        new_population = int(this_dict[key]["population"])
        if new_population > retrieved_smallest_population:
            retrieved_smallest_population = int(this_dict[key]["population"])
            smallest_province_name = key
    return smallest_province_name.title()


def get_province_description(province_name, this_dict):
    print()
    print("Return the string description of the province name")
    string_description = 'None'
    for key in this_dict.keys():
        if province_name.lower() == key.lower() and this_dict[key]["capital"] != this_dict[key]["largest"]:
            string_description = "%s has a population of %s whose capital is %s and largest city is %s." % (key.title(), this_dict[key]["population"], this_dict[key]["capital"].title(), this_dict[key]["largest"].title())
        elif province_name.lower() == key.lower() and this_dict[key]["capital"] == this_dict[key]["largest"]:
            string_description = "%s has a population of %s whose capital and largest city is %s." % (key.title(), this_dict[key]["population"], this_dict[key]["capital"].title())
    return string_description
