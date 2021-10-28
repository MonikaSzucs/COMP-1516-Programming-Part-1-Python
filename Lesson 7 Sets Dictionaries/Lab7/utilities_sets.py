def get_total_items(set1):
    print("Returns the total number of items for the given set1")
    return len(set1)


def display_all_items(set1):
    for items in set1:
        print(items)
    print()


def add_item(set1, item):
    print(set1)
    set1.add(item)
    print("Added 'cantaloupe' to the set and the resulting set is")
    display_all_items(set1)


def remove_item(set1, item):
    print("Removes the given item from the set")
    print(set1)
    set1.remove(item)
    return set1


def get_the_union_of(set1, set2):
    print("Returns a set of the union of the given set1 and set2")
    total_set = set1.union(set2)
    return total_set
