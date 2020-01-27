# -*- coding: utf-8 -*-
"""
Solution for Exercise 4.2

Avnika Manaktala

"""
#Importing Packages
from swampy.TurtleWorld import *
import math

#Creating Turtleworld and assigning turtle
world= TurtleWorld()
bob= Turtle()

#
def polyline(t,n,length, angle):
    """ Function creating polyline with 
        t= Turtle
        n=number of segments
        length= length of each segment
        angle= angle between each segment"""
        
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def arc(t,r,angle):
    """ Function creates arc with
        t=Turtle
        r=Radius of arc
        angle= angle that forms the arc"""
    arc_length= 2*math.pi*r*angle/360.0
    n= int(arc_length/3)+1
    step_length= arc_length/n
    step_angle= float(angle)/n
    polyline(t,n,step_length, step_angle)

def petal(t,r, angle):
    """Function creates a sigle petal with
        t=Turtle
        r= Radius of arcs
        angle=Angle that forms the arc"""
    for i in range(2):
        arc(t,r,angle)
        lt(t, 180-angle)
        
def flower(t,n,r,angle):
    """Function creates the flower with
        t=Turtle
        n=Number of petals
        r=Radius of arcs
        angle= Angle that forms the arcs"""
    for i in range(n):
        petal(t,r,angle)
        lt(t, 360/n)

def move(t,length):
    """Moves turtle a length without drawing the trail"""
    pu(t)
    fd(t, length)
    pd(t)

#Displaying flowers
move(bob, -150)
flower(bob,7, 50, 50)

move(bob, 150)
flower(bob,10, 50, 50)

move(bob, 300)
flower(bob,20, 50, 50)
wait_for_user()
