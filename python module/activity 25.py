#!/usr/bin/env python3
def count_words(filepath):

    dic = {}
    with open(filepath, 'r') as fp:
        t = fp.read().split()
        for w in t:
            if i in w:
                dic[i] = dic[w] +1
            else:
                dic[i] += 1
        return dic
    
    '''
    Count the occurrences of each word in the file. Create a dictionary that contains each word in the file as a key
    and the value for each key will contain the number of times each words is found in the file. Words will be
    separated by one or more whitespace characters spread over multiple lines.
       
    Args:
        filepath (str): The path to the file
    Returns:
        dict : keys - words
               values - number of times each word appears
    '''



# t = [l.strip() for l in fp.readlines() if l.strip() != ""] # for each l (line) in fp.readlines(): l will strip the white space for that string, and assign it to the list 't'
#     t = sorted(t, key = lambda x: x[9:15])
#     return t

filepath = 'python module/dictionary'
print(count_words(filepath))