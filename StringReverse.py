#!/usr/bin/env python
'''
A couple of functions to reverse an input string

'''

import math

 # Using python trick

def reverse_1(string):
    return string[::-1]
	
# O(logn) Solution

def reverse_2(string):
    string_list = list(string)
    for i in range(int((len(string))/2)):
        # Swap values in array.
        string_list[i], string_list[-1-i] = string_list[-1-i], string_list[i]
    return ''.join(string_list)

if __name__ == '__main__':
    # Test section
	print (reverse_1("My name is Ammad"))
	print (reverse_2("My name is Ammad"))