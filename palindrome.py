def palindrome (a):
    """
    Takes in a string and returns True if the string is a palindrome, False otherwise
    """
    # base case
    if len(a) == 1 or a == []:
        print("This is a palindrome")

    # recursion
    elif a[0] == a[-1]: #a[-1] is last element of string
        if len(a) == 2:
            print("This is a palindrome.")
        else:
            return palindrome(a[1:(len(a)-1)])
    else:
        return "not a palindrome"


print(palindrome("hannah"))
print(palindrome("racecar"))
print(palindrome("super"))


