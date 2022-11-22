#!/bin/usr/env python3
# Given an alphanumeric string, return the character whose ascii value is that of the integer represenation of all of the digits in the string concatenated in the order in which they appear.

# For example, given 'hell9oworld7', the returned character should be 'a' which has the ascii value of 97.

strng = 'hell9world7'
def q1(strng):
    lst = list(strng)
    digitsintext = []
    for char in lst:
        if char.isnumeric():
            digitsintext.append(char)
        else:
            pass
    return chr(int(''.join(digitsintext)))

q1(strng)