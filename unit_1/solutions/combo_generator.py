def yield_all_combos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.
    """
    items_len = len(items)
    for i in range(3 ** items_len):
        bag1 = []
        bag2 = []
        for j in range(items_len):
            bag = (i // (3 ** j)) % 3
            if bag == 1:
                bag1.append(items[j])
            elif bag == 2:
                bag2.append(items[j])

        print()
        yield bag1, bag2


items = [1, 2]
for bag_1, bag_2 in yield_all_combos(items):
    print('bag_1:', bag_1, ', bag_2: ', bag_2)
