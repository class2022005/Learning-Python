#!/usr/bin/env python3

# Given a positive integer, return its string representation with commas seperating groups of 3 digits.

# For example, given 65535 the returned string should be '65,535'.

def q1(n):
    # comma = '{:,}'.format(n)
    # print(comma)
    return '{:,}'.format(n)

q1(10000000)