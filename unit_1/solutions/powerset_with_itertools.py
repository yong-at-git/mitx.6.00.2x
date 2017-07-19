import itertools


def powerset(items):
    """
    Generates all combination of N items, i.e. the powerset of the items.
    :param items: a list of items
    :return: the powerset of the items
    """
    for i in range(len(items) + 1):
        for comb in itertools.combinations(items, i):
            yield comb
