#!/usr/bin/env python3

# Use python to produce code below that will perform the following:

# Given a mixed case string as parameter s
# Capitalize every letter with an even index within the string.
# Lowercase every letter with an odd index within the string.
# Return the resulting string.
# Example - Given: "ABCDEF ghijkl" Return: "AbCdEf gHiJkL"
s = 'asodjsioajdasiojdoajdioajdsio'
def leetString(s):
    leetTalk = list(s)
    for i, c in enumerate(leetTalk):
        if i%2==0:
            leetTalk[i] = c.upper()
        else:
            leetTalk[i] = c.lower()
    return ''.join(leetTalk)