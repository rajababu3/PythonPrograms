# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 12:14:23 2016

@author: Raja
"""
#==============================================================================
# Write a program that prints the number of times the string 'bob' occurs in s.
#  For example, if s = 'azcbobobegghakl', then your program should print
#  Number of times bob occurs is: 2
#==============================================================================

s = input("Enter a string: ")
bobCount = 0
for l in s:
    if l == 'b':
    if l == 'o':
        break
    if l=='b':
        bobCount +=1
print(bobCount)
