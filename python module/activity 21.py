#!/usr/bin/env python3
#Write a script that implements a function, find_product, which takes two numbers and returns the product. 
#Use the name=='__main__' idiom to prompt the user for two integers a print the result of calling find_product using those integers.
def find_product(int1, int2):
    return int1*int2

if __name__ == "__main__":
    input1 = int(input('Give me 1\n'))
    input2 = int(input('Give me 2\n'))
    print(find_product(input1, input2))

#Incorrect:test (__main__.TestAct21) ... File "34995db5-367a-4664-98ad-1725172666fb", line 40, in test actual = fp.getvalue().splitlines()[-1] 
# IndexError: list index out of range
