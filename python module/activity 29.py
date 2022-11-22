def sort_embedded(filepath):
    '''
    Read all lines from file in `filepath` and return a list of all lines sorted numerically by
    the number at character positions 10 to 15 in each line..
    Remove all linebreaks before sorting.
    
    Example: The embedded number is 561234 below.
    Here is a561234 long line of text from the file.
       
    Args:
        filepath (str): The path to the file
    Returns:
        list : lines from input file numerically sorted on the embedded number without linebreaks
    '''
    last = []
    with open(filepath, 'r') as fp:
        t = [l.strip() for l in fp.readlines() if l.strip() != ""] # for each l (line) in fp.readlines(): l will strip the white space for that string, and assign it to the list 't'
        
        # t = []
        # for l in fp.readlines():
        #     if l.strip() != "":
        #         t.append(l.strip())
        t = sorted(t, key = lambda x: x[9:15])
        return t
        # for lines in fp:
        #     t = lines[:-2]
        #     last.append(sorted(lines,fp[10:16]))
        # return last
filepath = '/home/usacys/Documents/Learning-Python/python module/activity29file'
sort_embedded(filepath)