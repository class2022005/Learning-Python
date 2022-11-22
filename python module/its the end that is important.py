#!/usr/bin/env python3
# Given a list (lst) and a number of items (n), return a new list containing the last n entries in lst.


def q1(lst,n):
    return lst[-n:]
q1([1, 2, 3, 4, 5, 6, 7, 8], 3)