#!/usr/bin/env python3

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