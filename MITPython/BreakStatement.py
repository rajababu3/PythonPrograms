# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 07:46:07 2016

@author: Raja
"""

mysum = 0
for i in range(3,10):
    mysum += i
    if mysum == 5:
        break
print(mysum)