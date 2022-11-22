#!/usr/bin/env python3

def make_tuple():
    '''
    Returns a tuple of the multiples of 10 from 1 to 100 inclusive.
    Args:
        None
    Returns:
        tuple: a tuple of the multiples of 10 from 1 to 100 inclusive
    '''
    tup = ()
    for i in range(1,101):
        if i % 10 == 0:
            tup = list(tup)
            tup.append(i)
            tup = tuple(tup)
    return tup

print(make_tuple())