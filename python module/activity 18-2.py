#!/usr/bin/env python3
# "You have a artist friend that likes to jot down some inspirational words when the mood strikes. 
# These fits of inspiration always have a theme that they need to remember with the messages. 
# Your friend needs some help keeping track. 
# Read each of the inspirational messages from the user and write them to the end of the file specified by fname. 
# ince the theme is important and must be remembered, add the theme and a colon before each message and ensure each inspirational message is on its own line. 
# An empty input will indicate no more entries and the end of the theme."
# Example:

# If theme was "Razzmatazz", and the input from the user was "I like nonsense; it wakes up the brain cells. - Dr. Seuss", the resulting string would be formated as follows: Razzmatazz:I like nonsense; it wakes up the brain cells. - Dr. Seuss

# Important:

# What if there are other lines to be added? What else seperates lines in a file? What needs to be added to the example line above?
# Do not overwrite the file. What mode should you open the file in?
def log_to_file(fname, theme):
    '''
    Args:
        fname (str): Path to an existing file that includes previous inspirational messages to keep.
        theme (str): Theme to be placed on each line.
    Returns:
        None
    '''
    inputLst = []
    uInput = input("Insert non-sense stuff")
    while True:
        if uInput != '':
            inputLst.append(f'{theme}:{uInput}')
        else:
            break
        uInput = input("Insert non-sense stuff")
    with open(fname, 'a') as fi:
        fi.write('\n'.join(inputLst))
        fi.write('\n')

log_to_file('act18_1.txt', 'Plumpkin')