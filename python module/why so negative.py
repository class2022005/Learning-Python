#!/usr/bin/env python3

#Given the argument numlist as a list of numbers, return True if all numbers in the list are NOT negative. If any numbers in the list are negative, return False.

def q1(numlist):
    for n in numlist:
      if n <= 0:
        return False
      else:
        return True

