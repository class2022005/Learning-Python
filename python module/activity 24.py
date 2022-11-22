#!/usr/bin/env python3
# import re
# def diffwords(fname, words):
#     lst = []
#     source = fname
#     pattern = words
#     wordlst = words.split(' ')
#     with open(fname, 'r+') as fi:
#         if re.match(fi, source):
#             print(fi)
#         else:
#             lst.append(match)
#         return lst
    
    
def diffwords(fname, words):
    lst = []
    with open(fname, 'r+') as fi:
        t = fi.read()
        r = t.split()
        for w in r:
            if w not in words:
                lst.append(w)
            else:
                pass
        return lst
            
      
fname = '/home/usacys/Documents/Learning-Python/python module/list'
# words = "test not ollie finn or bozo joke"
words = ['is', 'and', 'joke', 'test']
print(diffwords('/home/usacys/Documents/Learning-Python/python module/list', words))