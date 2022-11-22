#!/usr/bin/env python3

# Given a list of positive integers sorted in ascending order, return the first non-consecutive value. If all values are consecutive, return None.

# For example, given [1,2,3,4,6,7], the returned value should be 6.
arra = [1,2,3,4,6,7]
def q1(arr):
    arr1 = arr
    for n in arr:
        if n+1 == arr1[n+1]:
            pass
        elif n+1 != arr1[n+1]:
            return arr1[n+1]
        else:
            return 'None'
        
q1([1,2,3,4,6,7])