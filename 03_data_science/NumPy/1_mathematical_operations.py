# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 02:44:05 2026

@author: ahmed hamouda
"""

import numpy as np

a = np.sin(30)
b = np.cos(30)
c = np.tan(30)

d = np.sin(30*np.pi/180)
e = np.cos(30*np.pi/180)
f = np.tan(30*np.pi/180)

g = np.sin(np.deg2rad(30))
h = np.cos(np.deg2rad(30))
i = np.tan(np.deg2rad(30))

print(a,b,c)

print("---------------")

print(d,e,f)

print("---------------")

print(g,h,i)

j = np.round(3.674852)
k = np.round(3.674852,1)
l = np.round(3.674852,2)
m = np.round(3.674852,3)

print("---------------")

print(j,k,l,m)

n = np.floor(3.674852)
o = np.ceil(3.674852)

print("---------------")

print(n,o)

q = np.mod(20,7)
r = np.power(2,5)

print("---------------")

print(q,r)