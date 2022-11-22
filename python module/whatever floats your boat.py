#!/usr/bin/env python3
# Given the floatstr, which is a comma separated string of floats, return a list with each of the floats in the argument as elements in the list.

def q1(floatstr):

    fltLst = floatstr.split(',')
    for index, strFlt in enumerate(fltLst):
        fltLst[index] = float(strFlt)
    return fltLst

q1("1.2,72.3,74.5,7.7")