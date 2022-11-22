#!/usr/bin/env python3

# Use python to produce code below that will perform the following:

# Create a function called infinitearguments that will:
# Print to standard output all positional arguments, in the order received, on separate lines.
# Followed immediately by all keyword arguments in the form keyword=value in keyword alphabetic order.

def infinitearguments(*args, **kwargs): #infinitearguments(1,2,3,4,5,6,a=56,b=87,c=89,d=60)
    # print(*args,sep='\n')
    for a in args:
        print(a)
    for a in sorted(kwargs):
        print(f'{a}={kwargs[a]}')
    
    
    
    
infinitearguments(1,2,3,4,5,6,a=56,d=87,b=89,c=60,e=69,f=80)