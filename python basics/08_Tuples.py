# -*- coding: utf-8 -*-
"""
Created on Tue june 2 1:18:15 2026

@author: ahmed hamouda
"""
a = (1,2,3,4,5,6,7,8,9,10) #this is the tuple (we can not change the data that in the tuples)
# tuples like the lists but we write it inside the () not the []
b = (1,2.2,'ahmed') # we can have more than one datatype in the same tuple
print(b)
print(a[2]) # we called the elements inside the tuples in the same way like the lists
# the min , max , ... works for the tuple
#any try to append, add, sort to a tuple is not allowed
c = [1,2,3,4,5]
c= tuple(c) #convert the list c to a tuple
a = list(a) # convert the tuple a to list 
d = 1,2,3,4,5,6,7,8 #python deal with this as tuple
ages = [('ahmed','palestine',23),
        ('aymen','egypt',21),
        ('youssef','tunis',24),
        ('sara','sudan',18),
        ('sameh','libia',20)] # each element in this list is a tuple
# we can do sort for the ages var (its a list) even if the elements are tuples
newages = sorted(ages , key= lambda student : student[2]) # we sort depend on the age in this case
print(newages)
