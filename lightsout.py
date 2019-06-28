#
# hw3pr1.py - Lab problem: "Lights On!"
#
# Name:
#
#

import time           # provides time.sleep(0.5)
from random import *  # provides choice([0,1]), etc.
import sys            # larger recursive stack
sys.setrecursionlimit(10000) # 10000 stack frames availble

def timesTwo(i, oldL):
    """ Accepts an index (i) and an old list (oldL).
        mutate returns the ith element of a NEW list!
        * Note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve.
    """
    new_ith_element = oldL[i] * 2
    return new_ith_element

def sqr(i, oldL):
    """ Accepts an index (i) and an old list (oldL).
        mutate returns the ith element of a NEW list!
        * Note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve.
    """
    new_ith_element = oldL[i] ** 2
    return new_ith_element

def rot(i, oldL):
    """ Accepts an index (i) and an old list (oldL).
        mutate returns the ith element of a NEW list!
        * Note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve.
    """
    new_ith_element = oldL[i-1] 
    return new_ith_element

def rand(i, oldL):
    """ Accepts an index (i) and an old list (oldL).
        mutate returns the ith element of a NEW list!
        * Note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve.
    """
    new_ith_element = choice([0,1]) 
    return new_ith_element

def allOnes(L):
    """
    Accepts a list of integers L
    Returns True if all L's elements are 1; false otherwise
    """
    # base case: list was actually empty; return False
    if L == []:
        return False
    # as soon as you hit a 0, return False
    elif L[0] == 0:
        return False
    # if the list just has one value, 1, return True so we don't iterate down to blank
    elif len(L) == 1 and L[0] == 1:
        return True
    # recursive step
    else:   
        return allOnes(L[1:])

def mutate(i, oldL):
    """ Accepts an index (i) and an old list (oldL).
        mutate returns the ith element of a NEW list!
        * Note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve.
    """
    new_ith_element = 1 + oldL[i]
    return new_ith_element

def toggle(i, oldL, target = 0):
    """ Accepts an index (i), an old list (oldL) and the index to turn on (target).
        turn_on_one returns the ith element of a NEW list!
        * Note that turn_on_one returns ONLY the ith element
          turn_on_one thus needs to be called many times in evolve.
    """
    #TODO: add a test that target is in the range of available spaces in the list
    if i == target or i == target + 1 or i == target - 1:
        if oldL[i] == 0:
            new_ith_element = 1
               # this makes the game easy!
        else:
            new_ith_element = 0
    else:
        new_ith_element = oldL[i] # the new is the same as the old
    return new_ith_element

def evolve(oldL, mutate, curgen = 0):
    """ This function should evolve oldL (a list)
        it starts at curgen, the "current" generation
        and it ends at generation #5 (for now)
        
        It works by calling mutate at each index i.
    """
    print(oldL)                    
    print("  (gen: " + str(curgen) + ")")  # and its gen.
    time.sleep(0.5)
    
    if allOnes(oldL):  # we're done!
        return curgen
    else:
        user = int(input("Index? "))
        newL = [ mutate(i,oldL,user) for i in range(len(oldL)) ]

        return evolve(newL, mutate, curgen + 1)


evolve( [0,0,0,0], toggle )
#print(allOnes([0,0,0,0,1])) #False
#print(allOnes([1,1,1])) # True
#print(allOnes([])) #False
#print(allOnes([1,1,0])) # False


