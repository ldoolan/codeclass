def reduce(func, l, init):
    """ 
    Accepts a function of two arguments (func), a list (l) and an
    initial value. Applies func cumulatively to the items of l 
    from left to right, starting with the value in init, 
    so as to reduce the list to a single value.
    """

    # base case: empty list
    print(init)
    #if l == [] and :
    #    return []
    # recursive step
    # if: not last item in list
    #elif len(l) == 1:
        #return func(l[0], )
    # else: deal w/last item in list
    #else:
    return reduce(func, l[1:], func(l[0], init))

print(reduce(lambda x, y: x + y , [1, 2, 3, 4, 5], 0)) # == 15
print(reduce(lambda x, y: x * y , [1, 2, 3, 4, 5], 1)) # == 120
print(reduce(lambda x, y: x + ' ' + y , ['hello', 'bob'], '')) # == ' hello bob'
#assert reduce(lambda x, y: x + y , [1, 2, 3, 4, 5], 0) == 15
#assert reduce(lambda x, y: x * y , [1, 2, 3, 4, 5], 1) == 120
#assert reduce(lambda x, y: x + ' ' + y , ['hello', 'bob'], '') == 'hello bob'
