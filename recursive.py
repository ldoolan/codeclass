# Given a list of numbers, iterate over them recursively and find the biggest one

def biggest(L):
    """
    Takes a list of integers and returns the largest integer
    """
    # base case(s): list is 0 elements long, in which case call the biggest number 0;
    # or list is one element long, in which case return the element.
    print(type(L))
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        return L[0]
    # recursive step
    else:   
         return biggest(L[1:])

my_list = [1,2,3,2,1]
print(biggest(my_list))

