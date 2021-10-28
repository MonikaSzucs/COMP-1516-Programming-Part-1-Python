def display_all(this_dict):
    print(this_dict)
    for place in this_dict:
        print("%s is the capital city of %s" % (this_dict[place],place))


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
    pass


def get_another_capital_city(province_name, this_dict):
    pass


def get_largest_city(province_name, this_dict):
    pass


def get_smallest_province(this_dict):
    pass


def get_largest_province(this_dict):
    pass


def get_province_description(province_name, this_dict):
    pass

