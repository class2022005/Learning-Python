#!/usr/bin/env python3
# Given the variable length argument list, return the average of all the arguments as a float
from numpy import mean
def q1(*args):
    return sum(args)/len(args)