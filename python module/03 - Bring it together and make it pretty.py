#!/usr/bin/env python3

# Given two lists of integers, return a sorted list that contains all integers from both lists in descending order.

# For example, given [3,4,9] and [8,1,5] the returned list should be [9,8,5,4,3,1]. The returned list may contain duplicates.

def q1(lst0, lst1):
    lst3 = list(lst0 + lst1)
    lst3.sort(reverse=True)
    # print(lst3)
    return lst3

q1([1, 2, 3, 4, 5], [5, 6, 7, 8, 9])