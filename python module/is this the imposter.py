#!/usr/bin/env python3
# As you iterate through the given list, return the first duplicate value you come across.

# For example, if given [5,7,9,1,3,7,9,5], the returned value should be 7.

def q1(lst):
    res = set()
    for i in lst:
        if i in res:
            return i
        res.add(i)
    print(res)
  
q1([5,7,9,1,3,7,9,5])