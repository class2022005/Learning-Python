#!/usr/bin/env python3

lst = []

while True:
    data = input("enter data")
    print('data entered was {}'.format(data))
    if data.lower() == 'stop':
        break
    else:
        lst.append(data)

with open("myfile.txt", "w") as fp:
    fp.write(lst)

