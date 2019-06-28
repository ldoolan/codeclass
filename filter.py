def filter(pred, l):
    """ 
    Accepts a predicate (pred) and a list (l).
    Returns a new list containing only the items from l
    where pred(l) matches (returns true).
    """

    # base case: list is empty
    if l == []:
        return []
    # recursive step: list is not empty. Do 2 different things depending on whether pred is true for each thing
    else:
        if pred(l[0]):
            return [l[0]] + filter(pred, l[1:])
        else:
            return filter(pred, l[1:])
assert filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == [2, 4]
assert filter(lambda x: x % 3 != 0, [1, 2, 3, 4, 5]) == [1, 2, 4, 5]
