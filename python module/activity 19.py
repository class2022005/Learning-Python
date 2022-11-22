#!/usr/bin/env python3
import random
def grab(lst):
    '''
    Returns a randomly chosen item from the given list (lst).
    Args:
        lst (list): a list of items
    Returns:
        item (?): an item from the list
    '''    
    return random.choice(lst)
  
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
grab(lst)