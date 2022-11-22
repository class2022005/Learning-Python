#!/usr/bin/env python3

def count_bits(number):
    num_bits = bin(number)
    lst = list(num_bits)
    print(lst)
    value = 0
    for index in lst:
        if index == 1:
            value += 1
        else:
            pass
    return abs(value)


count_bits(0)
count_bits(7)
count_bits(9)
count_bits(10)
import codewars_test as test
from solution import count_bits

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it("Basic Tests")
#     def basic_tests():
#         test.assert_equals(count_bits(0), 0)
#         test.assert_equals(count_bits(7), 3)
#         test.assert_equals(count_bits(9), 2)
#         test.assert_equals(count_bits(10), 2)