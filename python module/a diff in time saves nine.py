#!/usr/bin/env python3

# Given two filenames, return a list whose elements consist of line numbers for which the two files differ. The first line is considered line 0.

def q1(f0, f1):
    with open(f0, 'r') as fi0, open(f1, 'r') as fi1:
        fi0 = fi0.readlines()
        fi1 = fi1.readlines()
        lineNumbers = []
        for index, line1 in enumerate(fi0):
            if line1 != fi1[index]:
                lineNumbers.append(index)
            else:
                pass
        return lineNumbers
q1('/home/usacys/python/python-1/rosso/test1.txt', '/home/usacys/python/python-1/rosso/test2.txt')

#expected ouput
# 2
# 4
# 5
# 6
