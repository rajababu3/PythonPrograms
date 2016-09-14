# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 12:14:23 2016

@author: Raja
"""

s = input("Enter a string: ")
bobCount = 0
for l in s:
    if l == 'b' or l == 'o' or l == 'b':
        bobCount +=1
print(bobCount)
