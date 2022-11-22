#!/usr/bin/env python3

# Given a sentence as a string with words being separated by a single space, return the length of the shortest word.

def q1(strng):
    sentence = strng.split(' ')
    x = min(sentence, key=len)
    if x == '':
      return ''
    else:
      return len(x)
      
    
strng = 'maybe it has the biggest wheels'
q1(strng)