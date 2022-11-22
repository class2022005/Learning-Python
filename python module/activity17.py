#!/usr/bin/env python3

# Return a list of ordinals for every character in the given string

# Hint: https://docs.python.org/3/library/functions.html#ord

def code_points(strng):
    lst = []
    for i in strng:
        lst.append(ord(i))
    return lst
print(code_points('08129u39012830921832091'))