#!/usr/bin/env python3

# Given 3 scores in the range [0-100] inclusive, return 'GO' if the average score is greater than 50. Otherwise return 'NOGO'.

def q1(s1,s2,s3):
    averag = (s1 + s2 + s3)/3
    if averag > 50:
        # print('GO')
        return 'GO'
    else:
        return 'NOGO'
        # print('NOGO')
q1(50, 40, 50)
q1(50, 60, 71)