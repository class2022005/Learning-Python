#!/usr/bin/env python3
import re
def diffwords(fname, words):
    lst = []
    source = fname
    pattern = words
    wordlst = words.split(' ')
    with open(fname, 'r+') as fi:
        if re.match(fi, source):
            print(fi)
        else:
            lst.append(match)
        return lst
    
    
# def diffwords(fname, words):
#     lst = []
#     with open(fname, 'r+') as fi:
#         t = fi.read()
#         t = t[1:-1]
#         r = t.split(',')
#         for w in r:
#             if w not in words:
#                 lst.append(w)
#             else:
#                 pass
#         return lst
            
      
fname = '/Users/hrosso/Sync/Cyber/Learning-Python/Learning-Python/python module/list'
words = "test not ollie finn or bozo"

print(diffwords('/Users/hrosso/Sync/Cyber/Learning-Python/Learning-Python/python module/list', words))