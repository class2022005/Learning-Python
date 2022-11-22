#!/usr/bin/env python3

# Given an input string, return a list containing the ordinal numbers of each character in the string in the order found in the input string.

def q1(strng):
    ordinalNumbers = []
    for index in strng:
        ordinalNumbers.append(ord(index))
    return ordinalNumbers

q1('string')