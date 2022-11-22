#!/usr/bin/env python3

# Use python to produce code below that will perform the following:

# Print out every even number on a separate line from parameters first to last, inclusive.
# Next print out every odd number from first to last, inclusive.

def evensandodds(first, last):
    even = []
    odd = []
    for index in range(first, last+1):
        if index % 2 == 0:
            even.append(str(index))
        else:
            odd.append(str(index))
    even = '\n'.join(even)
    odd = '\n'.join(odd)
    print(even)
    print(odd)

evensandodds(5, 13)