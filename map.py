def map(func, l):
    """ 
    Accepts a function (func) and a list (l).
    Returns a new list that is the result of applying func
    to every element of l.
    """
    # base case
    if l == []:
        return []

    # recursive step
    else:
        return [func(l[0])] + map(func, l[1:])
print(map(lambda x: x * 2, [1, 2, 3, 4, 5]) == [2, 4, 6, 8, 10])
assert map(len, ['hello', 'bob']) == [5, 3]
