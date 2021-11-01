"""
Assignment 1 by Monika Szucs A00878763
A script containing the get_total_items(set1), display_all_items(set1), add_item(set1, item), remove_item(set1, item),
get_the_union_of(set1, set2)
:author: Monika Szucs
:date: November 1, 2021
"""


def get_total_items(set1):
    """
        A function that returns the total number of items for the given set1
        First Variant, parameter, return
        :param set1: contains the set
        :return: the number of items within set1
    """
    print("Returns the total number of items for the given set1")
    return len(set1)


def display_all_items(set1):
    """
        A function that prints all the elements from set1 using iteration
        Second Variant and parameter
        :param set1: contains the set
    """
    for items in set1:
        print(items)
    print()


def add_item(set1, item):
    """
        A function that adds the given item to the set
        Third Variant, parameters
        :param set1: contains the set
        :param item: contains the new item to add to the set
    """
    print(set1)
    set1.add(item)
    print("Added 'cantaloupe' to the set and the resulting set is")
    display_all_items(set1)


def remove_item(set1, item):
    """
        A function that returns the updates set once the item has been removed
        Fourth Variant, parameters, return
        :param set1: contains the set
        :param item: specifies the item that wants to be removed from the set
        :return: the updates set after the item has been removed
    """
    print("Removes the given item from the set")
    print(set1)
    set1.remove(item)
    return set1


def get_the_union_of(set1, set2):
    """
        A function that returns a set of the union of the given set 1 and set 2
        Fifth Variant, parameters, return
        :param set1: contains the set
        :param set2: contains a second set
        :return: the set that unionized set1 and set 2
    """
    print("Returns a set of the union of the given set1 and set2")
    total_set = set1.union(set2)
    return total_set
