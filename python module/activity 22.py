#!/usr/bin/env python3

# Write a function, round_to_position, which takes a list of floats and returns a new list with the original floats each rounded 
# to the number of digits of precision after the decimal point corresponding to the original float's position in the list.

def round_to_position(lst):
    rounded = []
    strng = str(lst)
    for index, num in enumerate(lst):
        rounded.append(round(num, index))
    return rounded
# if __name__ = __main__:
#     round_to_position()

lst = [1,2,3.192,4.192,5.192,6.192,7.192,8.192,9.192,123.12312,1232131.123213131,123.2112]
round_to_position(lst)