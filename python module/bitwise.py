#!/usr/bin/env python3

# Create and return a number whose bits are set according to the following conditions:

# If the filename parameter is blank, set bit 0x1 in the return.
# If the overwrite parameter contains a value which evaluates to True, set bit 0x10 in the return.
# If the bytestowrite parameter is greater than 1,000,000, set bit 0x20 in the return.
# NOTE: There is no file to open for this question

def q1(filename, overwrite, bytestowrite):
    
    if filename == '':
      return set_bit('00010000', 2) #bitwise 0x1
    if overwrite == True:
      return set_bit('00010000', 2) #bitwise 0x10
    if bytestowrite > 1000000:
      return set_bit('001000000', 2) #bitwise 0x20