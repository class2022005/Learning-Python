#!/usr/bin/env python3
def strings():
    '''
    Returns a tuple of the following two strings:

    

    Physics is the universe's operating system

    Args:
        None
    Returns:
        tuple: a tuple of strings
     '''
    var1 = ""
    var2 = "Physics is the universe's operating system"
    tup = []
    tup.append(var1)
    tup.append(var2)
    tup = tuple(tup)
    return tup
print(strings())