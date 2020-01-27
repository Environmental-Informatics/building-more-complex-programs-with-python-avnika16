#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution for Exercise 7.1

Avnika Manaktala

"""
# Importing modules used
from math import sqrt
from tabulate import *

#Defining function to estimate square root of value a
def mysqrt(a):
    x= a-0.5 #Initial approximation of square root of a 
    while True: # Loop to estimate square root 
        y=(x + a/x)/2
        if abs(y-x)<0.0000001:
            return(x)
            break
        x=y
# Defining function to create table 
def test_square_root():
    results = [(a, mysqrt(a), math.sqrt(a), abs(math.sqrt(a)- mysqrt(a))) 
    for a in range(1, 10)]
    print(tabulate(results, headers=["num", "mysqrt(a)", "math.sqrt(a)", 
                                     "diff"]))
    
test_square_root() #Display table 
    