#!/usr/bin/env python3

# Given a string of multiple words separated by single spaces, return a new string with the sentence reversed. The words themselves should remain as they are.

# For example, given 'it is accepted as a masterpiece on strategy', the returned string should be 'strategy on masterpiece a as accepted is it'.

def q1(sentence):
    lst = sentence.split(' ')
    lst.reverse()
    return ' '.join(lst)
    # print(' '.join(lst))

q1('it is accepted as a masterpiece on strategy')