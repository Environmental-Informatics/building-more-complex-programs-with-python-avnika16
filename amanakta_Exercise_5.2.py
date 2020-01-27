#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution for Exercise 5.2

Avnika Manaktala
"""
def fermat(a,b,c,n): 
    #Defining Fermat's Theorem and conditional print statements
    if n>2 and (a**n) +(b**n)== (c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")
        
def user_fermat():
    #Defining user inputs
    a= float(input("Enter value for a: "))
    a=int(a)
    b= float(input("Enter value for b: "))
    b=int(b)
    c= float(input("Enter value for c: "))
    c=int(c)
    n= float(input("Enter value for n: "))
    n=int(n)
    fermat(a,b,c,n)
    
user_fermat() #Displaying function