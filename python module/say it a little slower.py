#!/usr/bin/env python3
# Given an input string, return a tuple with each element in the tuple containing a single word from the input string in order.

def q1(strng):
    tple = tuple(strng.split(' '))
    return tple
    # print(tple)
q1('string with things in the string')