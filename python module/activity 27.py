#!/usr/bin/env python3

def sort_ascii(filepath):
    '''
    Read all lines from file in `filepath` and return a list of all lines in case-insensitive ASCII order.
    Remove all linebreaks before sorting.
       
    Args:
        filepath (str): The path to the file
    Returns:
        list : lines from input file sorted into ASCII order without linebreaks
    '''
    lst = []
    
    with open(filepath, 'r') as fp:
        fp.readlines()
        for i in fp:
            lst.append(ascii(str.lower(fp.readlines()[i].strip('\n'))))
        print(lst)
        return sorted(lst)
    
filepath = '/Users/hrosso/Sync/Cyber/Learning-Python/Learning-Python/python module/multiple lines'

sort_ascii(filepath)