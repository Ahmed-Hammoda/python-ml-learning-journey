#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 03:46:27 2026

@author: ahmed hamoufa
"""
a = {1,2,12,1,2,15,59,18,9,4,5,2,4,6,164,9}
print(a) # sets removes duplicate elements and order them
b =list(a)
print(b) #its list but before that the the duplicate elements are removed then ordered the rest
c = {n*3 for n in range(20)} #another way to define a set
print(c)
print(a or c) # in this case python will take the smaller set
print(a and c) # in this case python will take the biger set
d = {"egypt", "KSA", "USA", "Argentine", "Russia"}
e = {"France" , "KSA", "Brazii" , "Panama" , "Japan" , "Jordan" , "Sudan" , "South Korea" , "Chile" , "egypt" , "lebanon"}
print(d | e) # the union between the two sets
print(d.intersection(e)) # to find the intersection between the sets
print(d.union(e)) #works like the (d | e)
print(d - e) # show the d set but remove any element in d that exists in e
print(d ^ e) #show d and e but remove any duplicate elements
