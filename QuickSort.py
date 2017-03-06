#!/usr/bin/env python
'''
QuickSort implementation in python using list comprehension

'''

import math,random

 # Function for quick sort
 
def quickSort(l):
    if len(l) <= 1:
        return []
    lesser = [x for x in l[1:] if x < l[0]]
    greater = [x for x in l[1:] if x > l[0]]
    return quickSort(lesser) + [l[0]] + quickSort(greater)



if __name__ == '__main__':
    # Test section
	list = [5,8,3,1,2,7,9,6]
	result=quickSort(list)
	print(result)