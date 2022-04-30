import math

a = int(input('Insert on of the known lengths for the triangle:'))
b = int(input('Insert on of the other known lengths for the triangle:'))
c = math.hypot(a, b)
print(f'The hypotenuse of this triangle is {c}')
