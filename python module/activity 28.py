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
        t = [l.strip() for l in fp.readlines() if l.strip() != ""]
        t = sorted(t, key = lambda x: len(x), reverse=True)
        return t
    
    # t = [l.strip() for l in fp.readlines() if l.strip() != ""] # for each l (line) in fp.readlines(): l will strip the white space for that string, and assign it to the list 't'
    #     t = sorted(t, key = lambda x: x[9:15])
    #     return t
    
filepath = '/home/usacys/Documents/Learning-Python/python module/multiple lines'

print(sort_length(filepath))