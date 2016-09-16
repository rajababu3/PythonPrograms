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
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        bobCount +=1
print(bobCount)
