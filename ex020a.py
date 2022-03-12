import random

r1 = str(input('First Student:'))
r2 = str(input('Second Student:'))
r3 = str(input('Third Student:'))
r4 = str(input('Fourth Student:'))
list = [r1, r2, r3, r4]
random.shuffle(list)
print('The random selection of the students is: ')
print(list)