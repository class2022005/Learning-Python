import random

r1 = input('Enter the name of the first student:')
r2 = input('Enter the name of the second student:')
r3 = input('Enter the name of the third student:')
r4 = input('Enter the name of the forth student:')
list = [r1, r2, r3, r4]
print(f'The lucky winner is: {random.choice(list)}')


# https://docs.python.org/release/3.10.2/library/random.html#module-random