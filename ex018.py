import math
degree = int(input('Insert an angle to find its Sine, Cossine, and Tangent values:'))
angle = math.radians(degree)
print(f'The Sine of {degree} is {math.sin(angle):.2f}')
print(f'The Cossine of {degree} is {math.cos(angle):2f}')
print(f'The Tangent of {degree} is {math.tan(angle):2f}')