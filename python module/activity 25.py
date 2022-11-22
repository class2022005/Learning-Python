#!/usr/bin/env python3
import re
def count_words(filepath):
    '''
    Count the occurrences of each word in the file. Create a dictionary that contains each word in the file as a key
    and the value for each key will contain the number of times each words is found in the file. Words will be
    separated by one or more whitespace characters spread over multiple lines.
       
    Args:
        filepath (str): The path to the file
    Returns:
        dict : keys - words
               values - number of times each word appears
    '''
    dic = {}
    with open(filepath, 'r') as fp:
        for i, w in enumerate(fp):
            i, w = fp.split()
            dic[int(i)] = w
        return dic





filepath = '/Users/hrosso/Sync/Cyber/Learning-Python/Learning-Python/python module/list'
print(count_words(filepath))