#!/usr/bin/env python3
# Replace all found instances of the individual tuple entries in the file found at in_path. 
# Replacements will be in the list reps as a list of tuples. 
# Each tuple entry will contain the 'find' as the first element and the 'replace' will be the second element. 
# Write the result to the file specified with out_path.

# Example:

# List of Tuples example - [("taken","delivered"),("cat","dog"),("outside","beyond"),("straightaway","forthwith"),("possibly","perchance")]
# Original string example - "The cat possibly needs to be taken outside, straightaway."
# Changed string example - "The dog perchance needs to be delivered beyond, forthwith."
def replace_in_file(in_path, out_path, reps):
    '''
    Args:
        in_path (str): input file path
        out_path (str): output file path
        reps (list): list of tuples containing ("find", "replace") mappings
    Returns:
        None
    '''
    dictionary = dict(reps)
    with open(in_path, 'r') as fi, open(out_path, 'w') as fo:
        for index, words in enumerate(fi.readlines()):
            words_copy = words
            for word in dictionary:
                words_copy = words_copy.replace(word, dictionary[word])
            fo.write(words_copy)


replace_in_file('/home/usacys/python/python-1/rosso/in_path', 'act18_1.txt',[("taken","delivered"),("cat","dog"),("outside","beyond"),("straightaway","forthwith"),("possibly","perchance")])