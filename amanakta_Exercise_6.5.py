#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution for Exercise 6.5

Avnika Manaktala
"""

def gcd(a,b):
    #Defining GCD function
    if b!=0: #Setting up recursion
        return gcd(b, a%b)
    else:
        return a #When b=0 recursion stops


def user_gcd():
    #Defining user input for GCD function
    a= int(input("Enter a: "))
    a= float(a)
    b= int(input("Enter b: "))
    b= float(b)
    print("GCD= ", gcd(a,b))

user_gcd() #Running Function

