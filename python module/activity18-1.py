#!/usr/bin/env python3
# "Sometimes my cousin is just mean. He sent me a file with a special message but made it into a crazy series of ones and zeros. 
# He told me each letter was on its own line, and could be converted into an Unicode character. Can you help me by decoding his message?"

# Each line will be a string character. You will need to convert the string Ones and Zeros into an integer 
# (but these are not base 10, so keep that in mind) and then pass that data to code that will convert it to its corresponding Unicode character. 
# Thanks to Python's "batteries included" philosophy, there are two Python built-in functions that can help handle this for you.

def tough_read(fname):
    '''
    Args:
        fname (str): path to a file where the input is located
    Returns:
        str: Sentence that was decoded
    '''
    with open(fname, 'r') as fi:
        #fi = open(fname, 'r')
        #fo = open(fname, 'w')
        lst = []
        for line in fi.readlines():
            tmp = chr(int(line,base=2))
            lst.append(tmp)
            #tmp = chr(tmp)
            #lst.append(tmp)
            #print(line)
        return "".join(lst)

fname= '/home/usacys/python/python-1/rosso/inpath'
print(tough_read('act18_1.txt'))