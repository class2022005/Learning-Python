#!/usr/bin/env python3
# FIZZ BUZZ
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