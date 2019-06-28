from functools import reduce

def add(x, y):
     '''Returns the sum of the two
             arguments.'''
     return x + y
 
def triple(x):
     '''Takes a number x as an argument
             and returns 3 * x.'''
     return 3 * x

def mapReduce(mapFunction, reduceFunction, myList):
    '''Applies mapFunction to myList to
            construct a new list and then
            applies reduceFunction to the
            new list and returns
            reduceFunction's result.'''

    newList = map(mapFunction, myList)
    value = reduce(reduceFunction, newList)
    return value

print (mapReduce(triple, add, [14, 10, 12, 5]))