#!/usr/bin/env python3

sentence = 'abracadabra'
def get_count(sentence):
    count = 0
    for s in list(sentence):
        if s == 'y':
            count += 0
        elif s == 'a' or 'e' or 'i' or 'o' or 'u':
            count += 1
        else:
            count += 0
    return count
print(get_count(sentence))