# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:30:22 2026

@author: ahmed hamouda
"""

#how to import library in python
# import math
# from math import factorial,sin
#from math import *
# OR (the best)
import math as m # in this case we can use m as a var name in the code

c = m.exp(7)
print(c)

a = m.log(7 , 49)
print(a)

print(m.radians(20))
print(m.degrees(3.14))
print(m.sin(m.radians(30))) # if you want to use the sin,cos,tan,... the angle should be in radian
print(m.pi , m.tau , m.e , m.inf) # important constants
print (m.copysign(8, -6)) # here the function will copy the - form the -6 and put it for the 8
print(m.ceil(20.1))
print(m.floor(20.8))
print(m.erf(20))
print(m.gamma(20))