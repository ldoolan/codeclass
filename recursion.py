# add_list: sun a list of integers
"""
Accepts a list of integers and returns an integer representing the sum
If the list is empty, return 0
"""
def add_list(L):
    # base case
    # if list is empty, return 0
    if L == []:
        return 0

    # recursive step
    return L[0] + add_list(L[1:])


# factorial: Given a positive number, return the factorial of that number.
"""
Accepts a positive integer and returns an integer represeting the factorial of the input
"""
def factorial(n):
    # base case
    if n == 1:
        return 1
    # recursive step
    return n * factorial(n - 1)