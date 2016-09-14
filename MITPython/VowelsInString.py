# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 12:14:26 2016

@author: Raja
"""

s = input("Enter String: ")
vowelCount = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        vowelCount +=1
print(vowelCount)