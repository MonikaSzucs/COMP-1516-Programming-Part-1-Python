import locale


def display_all(this_dict):
    print(this_dict)
    for place in this_dict:
        print("%s is the capital city of %s" % (this_dict[place], place))


def get_capital_city(province_name, this_dict):
    print()
    print("Returns the capital city for the given province name in the given dictionary")
    matching_province_name = ""
    for place in this_dict:
        if place == province_name:
            matching_province_name = this_dict[place]
    return matching_province_name


def add_element(province_name, capital_city, this_dict):
    print("Adds the given key-value")
    this_dict[province_name] = capital_city
    print(this_dict)


def remove_item(province_name, this_dict):
    print("Removes the given key from the dictionary")
    del this_dict[province_name]
    print(this_dict)


def get_total_population(this_dict):
    print()
    print("Returns the total population of this_dict by summing up the population of each province: ")
    population_number = 0
    for key in this_dict.keys():
        population_number += int(this_dict[key]["population"])
    locale.setlocale(locale.LC_ALL, 'en_US')
    return locale.format("%d", population_number, grouping=True)


def get_another_capital_city(province_name, this_dict):
    print()
    print("Returns the name of the capital city for the given province_name")
    retrieved_capital_city_name = "None"
    for key in this_dict.keys():
        if key == province_name.lower():
            retrieved_capital_city_name = this_dict[key]["capital"].title()
    return retrieved_capital_city_name


def get_largest_city(province_name, this_dict):
    print()
    print("Returns the name of teh largest city for the given province name")
    retrieved_population = 'None'
    for key in this_dict.keys():
        if key == province_name.lower():
            retrieved_population = this_dict[key]["largest"].title()
    return retrieved_population


def get_smallest_province(this_dict):
    print()
    print("Returns the name of the province with the smallest population")
    retrieved_smallest_population = 999999999
    smallest_province_name = ''
    for key in this_dict.keys():
        new_population = int(this_dict[key]["population"])
        if new_population < retrieved_smallest_population:
            retrieved_smallest_population = int(this_dict[key]["population"])
            smallest_province_name = key
    return smallest_province_name.title()


def get_largest_province(this_dict):
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
    pass
