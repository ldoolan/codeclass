def filter(pred, l):
    """ Accepts a predicate (pred) and a list (l).
        Returns a new list containing only the items from l
        where pred(l) matches (returns true).
    """

assert filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == [2, 4]
assert filter(lambda x: x % 3 != 0, [1, 2, 3, 4, 5]) == [1, 2, 4, 5]
