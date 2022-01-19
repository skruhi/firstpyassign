# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import pi

r = float(input ("Enter radius of circle : "))

print ("Area of the circle is: " + str(pi * r**2))


filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
