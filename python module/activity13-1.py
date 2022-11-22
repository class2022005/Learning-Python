#!/usr/bin/env python3
def make_tuple(a,b):
    '''
    Returns a tuple of the multiples of 10 from a to b inclusive.
    Args:
        None
    Returns:
        tuple: a tuple of the multiples of 10 from a to b inclusive
    '''    
    tup = ()
    if b < a:
        a, b = b, a
    for i in range(a,b+1):
        if i % 10 == 0:
            tup = list(tup)
            tup.append(i)
            tup = tuple(tup)        
    return tup
print(make_tuple(20,1))