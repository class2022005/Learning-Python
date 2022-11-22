#!/bin/usr/env python3

# Given a filename, open the file and return the length of the first line in the file excluding the line terminator.

def q1(filename):
    with open(filename, 'r') as fi:
        first_line = fi.readlines()[0].strip('\n')
        return len(first_line)
        # print(len(first_line))


q1('/home/usacys/python/python-1/rosso/outpath')