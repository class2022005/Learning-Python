#!/usr/bin/env python3
def reverse_string(strng):
    '''
    Returns a copy of the given string reversed
    Args:
        strng (str): a string of alphanumeric characters
    Returns:
        str: a copy of the given string reversed
    '''    
    strng = list(strng)
    return ''.join(reversed(strng))

print(reverse_string('12341234'))