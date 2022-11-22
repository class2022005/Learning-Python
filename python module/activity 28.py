#!/usr/bin/env python3

def sort_length(filepath):
    '''
    Read all lines from file in `filepath` and return a list of all lines sorted longest to shortest.
    Remove all linebreaks before sorting.
       
    Args:
        filepath (str): The path to the file
    Returns:
        list : lines from input file sorted longest to shortest without linebreaks
    '''
    stripped = []
    # filepath = list(filepath)
    with open(filepath, 'r+') as fp:
        for i in fp:
            stripped.append(str(fp.readlines()[i].strip('\n')))
        return sorted(stripped,key=len)
    
    
    
filepath = '/Users/hrosso/Sync/Cyber/Learning-Python/Learning-Python/python module/multiple lines'

sort_length(filepath)