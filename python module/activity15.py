#!/usr/bin/env python3

def disect(lst):
    '''
    Returns a tuple of the given list split into two equally sized halves.
    The given list will always consist of an even number of elements.
    Args:
        lst (lst): a list of elements
    Returns:
        tuple: a tuple of two lists
    '''
        
    var1 = len(lst) // 2
    lst1 = lst[0:var1]
    lst2 = lst[var1:]
    tup = tuple([lst1, lst2])
    return tup
print(disect([1, 2, 3, 4, 5, 6]))