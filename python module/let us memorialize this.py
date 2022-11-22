#!/usr/bin/env python3
# Given a filename and a list, write each entry from the list to the file on separate lines until a case-insensitive entry of 
# "stop" is found in the list. If "stop" is not found in the list, write the entire list to the file on separate lines.

def q1(filename,lst):
    with open(filename, 'w') as fi:
        for line in lst:
            if line != "stop":
                fi.write(line + '\n')
            else:
                break

lst = ['12', '221', '221312', 'stop', 'just kidding']
q1('/home/usacys/python/python-1/rosso/outpath',lst)