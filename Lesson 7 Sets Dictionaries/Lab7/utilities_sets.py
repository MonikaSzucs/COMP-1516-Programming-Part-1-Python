def get_total_items(set1):
    print("get_total_items")
    return len(set1)


def display_all_items(set1):
    for items in set1:
        print(items)


def add_item(set1, item):
    print()
    print(list(set1))
    set1 = list(set1)
    set1.append(item)
    print(set1)
    print("Added 'cantaloupe' to the set and the resulting set is")
    return set1


def remove_item(set1, item):
    pass

def get_the_union_of(set1, set2):
    pass