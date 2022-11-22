#!/usr/bin/env python3
#Activity 1
# Use python to produce code below that will create several named variables with the specified value:

# Identifier	Value	Type
# hello	hello	string
# is_python_awesome	true	boolean
# days_in_python	6	integer
# pie_size	3.14	float
# NOTE: Do not indent your code
#!/usr/bin/env python3
hello = 'hello'
is_python_awesome = True
days_in_python = 6
pie_size = 3.14


#Activity 2
# Use Python to produce code below that will convert the provided literal ("Starting Value"), convert it to the indicated data type by using the appropriate Python Built-in Function(s), and assign the output to the named variable as designated below.

# Task	Identifier	Starting Value	Convert to Type
# string to int	int_input	"345"	int
# string to float	pi_4	"3.1415"	float
# int to string	hours_str	40	string
# int to float	hourly_rate	15	float
# NOTE: Conversion functions must be called
# NOTE: Do not indent your code

#!/usr/bin/env python3

int_input = int("345")
pi_4 = float("3.1415")
hours_str = str(40)
hourly_rate = float(15)

#Activity 3
#!/usr/bin/env python3

x = 16
y = 3
xysum = x + y
xydiff = x - y
xyprod = x * y
xyquo = x / y
xyintquo = x // y
xymod = x % y

#Activity 4

name = 'Jerry'
greeting = 'Sir'
time = 'noon'
output = f'Hello {name}! {greeting}, will you be arriving by {time}?'

#activity 5

sentence = 'good for all'
sent_list = list(sentence)
sent_list[0] = 'f'
sent_list[-1] = '?'
output = '.'.join(sent_list)

#activity 0
# Use python to produce code below that will:

# Given an email address in email
# Convert the email into a list named `lst'
# The list will contain all individual parts of the email
# Example: email = 'alan.m.turing@genius.com' -> lst = ['alan','m','turing', 'genius', 'com']
# NOTE: A variable named email will be available to your code when running.
# NOTE: You must create a variable named lst which contains the required data.
# NOTE: Do not indent your code
lst = email.replace('@', '.')
lst = lst.split('.')

#activity 6
# Use python to produce code below that will perform the following:

# Read multiple numbers separated by spaces on the same line from the user.
# Change all spaces to a plus sign.
# Print the resulting string to the user.
# NOTE: Do not indent your code

num_str = input("Enter a lot of numbers with spaces")
num_plus = num_str.replace(' ', '+')
print(num_plus)

#Activity 7
# Use python to produce code below that will perform the following:

# Read input from the user, the input will be an integer.
# Determine which of the following categories the number fits into an print this to the user:
# Negative Even
# Negative Odd
# Zero
# Positive Even
# Positive Odd
numInput = int(input("Enter a number, and I'll tell you what it is"))
if numInput < 0 and numInput % 2 == 0:
    print("Negative Even")
elif numInput < 0:
    print("Negative Odd")
elif numInput > 0 and numInput % 2 == 0:
    print("Positive Even")
elif numInput > 0:
    print("Positive Odd")
else:
    print("Zero")
    
#Activity 00A
fizBuz = int(input("give me a numbah"))
fiuz = ''
if fizBuz % 3 == 0:
    fiuz += "fizz"
if fizBuz % 5 == 0:
    fiuz += "buzz"
if fiuz == '':
    print(fizBuz)
else:
    print(fiuz)
    
#Activity 8
# Use python to produce code below that will perform the following:

# Create a function named domath that will accept 3 parameters.
# The function will add the first two parameters and multiply this sum by the third parameter.
# You can select the identifiers for each of the parameters.
# The resulting product will be returned to the caller.
def domath(var1, var2, var3):
    return (var1 + var2) * var3

#Activity 9
# UserDict pythonapi to produce code below that will perform the following:

# Read multiple lines from the user on standard input until an empty string is read.
# Return a list of all these lines without line terminators
# Each line should be reversed from how it is read in.

def reverseit():
    userInput = ''
    userLst = []
    while True:
        userInput = input("Strings?")
        if userInput != '':
            userInput = ''.join(list(reversed(userInput)))
            userLst.append(userInput)
        else:
            break
    return userLst

#Activity 00B
def guess_number(n):
    while True:
        guess = int(input("Give me a numbah!!! (0-100)"))
        if guess == n:
            print("WIN")
            break
        elif guess > n:
            print("too high")
        elif guess < n:
            print("too low")
guess_number(23)

#Activity 10
# Use python to produce code below that will perform the following:

# Given a mixed case string as parameter s
# Capitalize every letter with an even index within the string.
# Lowercase every letter with an odd index within the string.
# Return the resulting string.
# Example - Given: "ABCDEF ghijkl" Return: "AbCdEf gHiJkL"
def leetString(s):
    leetTalk = list(s)
    for i, c in enumerate(leetTalk):
        if i%2==0:
            leetTalk[i] = c.upper()
        else:
            leetTalk[i] = c.lower()
    return ''.join(leetTalk)

#Activity 11
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
    
#Activity 12
def user_io():
    '''
    Returns a list of items read from the user until the user enters an empty string.

    Args:
        None
    Returns:
        list: a list of strings
    '''    
    database = []
    while True:
        givemestuff = input("Give me stringgssssssss")
        if givemestuff != '':
            database.append(givemestuff)
        elif givemestuff == '':
            break
    return database

#Activity 13
def make_tuple():
    '''
    Returns a tuple of the multiples of 10 from 1 to 100 inclusive.
    Args:
        None
    Returns:
        tuple: a tuple of the multiples of 10 from 1 to 100 inclusive
    '''
    tup = ()
    for i in range(1,101):
        if i % 10 == 0:
            tup = list(tup)
            tup.append(i)
            tup = tuple(tup)
    return tup

#Activity 13-1
def make_tuple(a,b):
    '''
    Returns a tuple of the multiples of 10 from a to b inclusive.
    Args:
        None
    Returns:
        tuple: a tuple of the multiples of 10 from a to b inclusive
    '''    
    tup = ()
    if b < a:
        a, b = b, a
    for i in range(a,b+1):
        if i % 10 == 0:
            tup = list(tup)
            tup.append(i)
            tup = tuple(tup)        
    return tup

#Activity 14
def strings():
    '''
    Returns a tuple of the following two strings:

    

    Physics is the universe's operating system

    Args:
        None
    Returns:
        tuple: a tuple of strings
     '''
    var1 = ""
    var2 = "Physics is the universe's operating system"
    tup = []
    tup.append(var1)
    tup.append(var2)
    tup = tuple(tup)
    return tup

#Activity 15
def disect(lst):
    '''
    Returns a tuple of the given list split into two equally sized halves.
    The given list will always consist of an even number of elements.
    Args:
        lst (lst): a list of elements
    Returns:
        tuple: a tuple of two lists
    '''
        
    var1 = len(lst) // 2
    lst1 = lst[0:var1]
    lst2 = lst[var1:]
    tup = tuple([lst1, lst2])
    return tup

#Activity 16
def reverse_string(strng):
    '''
    Returns a copy of the given string reversed
    Args:
        strng (str): a string of alphanumeric characters
    Returns:
        str: a copy of the given string reversed
    '''    
    strng = list(strng)
    return ''.join(reversed(strng))

#Activity 17
def code_points(strng):
    lst = []
    for i in strng:
        lst.append(ord(i))
    return lst

#Activity 18
# Use python to produce code below that will perform the following:

# Read file specified by the path in inpath parameter and write all lines to the file specified by the outpath parameter.
# Before writing out each line, add the line number starting with 1 follow by colon and space.
def linenums(inpath, outpath):
    # with pen inpath as fi,
    fi = open(inpath, 'r')
    fo = open(outpath, 'w')
    for i, line in enumerate(fi.readlines()):
        tmp = line
        tmp = f'{i+1}: ' + tmp
        fo.write(tmp)
    fi.close()
    fo.close()

#Activity 18-1
# "Sometimes my cousin is just mean. He sent me a file with a special message but made it into a crazy series of ones and zeros. He told me each letter was on its own line, and could be converted into an Unicode character. Can you help me by decoding his message?"
# Each line will be a string character. You will need to convert the string Ones and Zeros into an integer (but these are not base 10, so keep that in mind) and then pass that data to code that will convert it to its corresponding Unicode character. Thanks to Python's "batteries included" philosophy, there are two Python built-in functions that can help handle this for you.
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
            tmp = chr(int(line.strip(),base=2))
            lst.append(tmp)
            #tmp = chr(tmp)
            #lst.append(tmp)
            #print(line)
        return "".join(lst)

#Activity 18-2
def log_to_file(fname, theme):
    '''
    Args:
        fname (str): Path to an existing file that includes previous inspirational messages to keep.
        theme (str): Theme to be placed on each line.
    Returns:
        None
    '''
    inputLst = []
    uInput = input("Insert non-sense stuff")
    while True:
        if uInput != '':
            inputLst.append(f'{theme}:{uInput}')
        else:
            break
        uInput = input("Insert non-sense stuff")
    with open(fname, 'a') as fi:
        fi.write('\n'.join(inputLst))
        fi.write('\n')
    
#Activity 18-3
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
            
#Activity 19
import random
def grab(lst):
    '''
    Returns a randomly chosen item from the given list (lst).
    Args:
        lst (list): a list of items
    Returns:
        item (?): an item from the list
    '''    
    return random.choice(lst)

#Activity 20

import hashlib
def get_hash(data="python"):
    '''
    Returns the SHA3 256-bit hash of the data provided.
    You will need to use the hashlib python library to complete this challenge.
       
    NOTE: The first call will use the string "python" later calls will use random strings
    NOTE: You can convert a string into a bytes-like object which is needed for hashing with: 
             
    data.encode("utf-8")
    
    NOTE: You can create a bytes-like object out of a literal by adding a b in front of the string, ie b"python" or b'python'
       
    Args:
        data (str): data to be encoded
    Returns:
        str : The SHA3 256-bit hash of the provided data
    '''    
    encoded = data.encode("utf-8")
    return hashlib.sha3_256(encoded).hexdigest()

#Activity 21

def find_product(int1, int2):
    return int1*int2

if __name__ == "__main__":
    input1 = int(input('Give me 1\n'))
    input2 = int(input('Give me 2\n'))
    print(find_product(input1, input2))
    
#Activity 22
def round_to_position(lst):
    rounded = []
    strng = str(lst)
    for index, num in enumerate(lst):
        rounded.append(round(num, index))
    return rounded

#Activity 23
def get_type_str(obj):
    '''
    Returns the type of the parameter as a string.
    Possible types are:
string
boolean
integer 
float  
list 
tuple
    NOTE: Any other types should be identified with 'unknown'
       
    Args:
        obj (?): The object that should be classified
    Returns:
        str : The type of the provided data
    '''   
    if type(obj) is tuple:
        return 'tuple'
    elif type(obj) is bool:
        return 'boolean'
    elif type(obj) is int:
        return 'integer'
    elif type(obj) is list:
        return 'list'
    elif type(obj) is float:
        return 'float'
    elif type(obj) is str:
        return 'string'
    elif type(obj) is not (tuple, str, int, list, bool, float):
        return 'unknown'
    
#Activity 24
# Use python to produce code below that will perform the following:

# A list of words is provided in the file specified by fname.
# Another list of words is provided as the parameter words.
# Return a list of all the words found in the file that are NOT contained in the list of words in parameter.
# Each word in the file will be separated by at least one character of whitespace.
def diffwords(fname, words):
    lst = []
    fname = list(fname)
    words_length = len(words)
    with open(fname, 'w') as fi:
        for i, w in enumerate(fi):
            if w != words[i]:
                lst.append(w)
            elif w == words[i]:
                pass
        return ' '.join(lst)



#Activity 25

#Activity 26

#Activity 27

#Activity 28

#Activity 29

#Activity 120

def numsys(startint):
    """ Given an integer `startint`, convert this integer to its 
    binary version, octal version, and hexadecimal version and 
    return these as a tuple in the order given. """
    return bin(startint), oct(startint), hex(startint)
    
def getints(binnum, octnum, decnum, hexnum):
    """ Given the string parameters `binnum` (binary number), 
    `octnum` (octal number), decnum` (decimal number), `hexnum` 
    (hexadecimal number), convert each of these  to an integer and 
    return them as a list in their parameter order. """
    return [int(binnum, 2), int(octnum, 8), int(decnum, 10), int(hexnum, 16)]
    
def literals():
    """ Create a list and set the value using literals and return 
    the list. All literals will represent the decimal integer value 
    1,000,000 (one million). You must use a literal to represent 
    the target value in binary, hexadecimal, decimal, and octal.
    The order is not important. """
    literal = '1000000'
    return [int('0b11110100001001000000', 2), int('0xf4240', 16), 1000000, int('0o3641100', 8)]
