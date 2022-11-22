#!/usr/bin/env python3

def user_io():
    '''
    Returns a list of items read from the user until the user enters an empty string.

    Args:
        None
    Returns:
        list: a list of strings
    '''    
    database = []
    while True:
        givemestuff = input("Give me stringgssssssss")
        if givemestuff != '':
            database.append(givemestuff)
        elif givemestuff == '':
            break
    return database
print(user_io())