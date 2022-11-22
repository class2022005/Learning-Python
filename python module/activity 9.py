#!/usr/bin/env python3'

# Use python to produce code below that will perform the following:

# Read multiple lines from the user on standard input until an empty string is read.
# Return a list of all these lines without line terminators
# Each line should be reversed from how it is read in.

def reverseit():
    userInput = ''
    userLst = []
    while True:
        userInput = input("Strings?")
        if userInput != '':
            userInput = ''.join(list(reversed(userInput)))
            userLst.append(userInput)
        else:
            break
    return userLst
print(reverseit())