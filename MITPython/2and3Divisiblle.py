# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 08:06:53 2016

@author: Raja
"""

x = int(input("Enter a number: "))

if x % 2 == 0:
    if x % 3 == 0:
        print('Its multiple of 2 and 3')
    else:
        print('It is divisible by 2 only')
else:
    print('Divisible by 3 only')