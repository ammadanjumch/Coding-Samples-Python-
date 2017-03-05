#!/usr/bin/env python
'''
Factorial
Input: Take in a number
Output: The factorial of a number (n!). The product of all positive integers less than or equal to a number.
'''

import math

 # Recursive solution

def rec_fact(n):
    if n == 0:
        return 1
    else:
        return (n * rec_fact(n - 1))

# While loop iteration solution - O(n)

def loop_sol_1(n):
    if n == 0:
        n = 1
    num = n
    while num > 1:
        num -= 1
        n *= num
    return n


if __name__ == '__main__':
    # Test section
	print (loop_sol_1(10))
	print (rec_fact(10))