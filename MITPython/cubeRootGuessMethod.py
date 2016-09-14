# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 09:34:41 2016

@author: Raja
"""
#This will work only for integer
cube = int(input("Enter a number: "))
for guess in range(abs(cube + 1)):
    if guess**3 >= abs(cube):
        break
if guess != abs(cube):
    print(cube," is not perfeect cube")
else:
    if cube < 0:
        guess = - guess
    print("Cube root if ", cube, "is", guess)