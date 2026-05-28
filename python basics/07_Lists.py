# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:11:59 2026

@author: ahmed hamouda
"""
# in python you defined the lists with [] 
# you can put more than one datatype in the same list
# you can do list inside list
a = ['ahmed',12,3+5j,True] # this is the noraml list with more than one datatype
print(a)
b = [['ahmed','hamouda'],[23,'nov'],'engineer'] # list inside list
c = [1,2,3,4,5,6,7,8,9,10]
print(b)
print(list('python')) #take each letter in the string as an element in the list
print(a[3]) # to get the fourth element in the a list because the list index start from 0
print(c[3:7]) #take from the fourth to the seventh element in the c list (we do not take the 8th one)
print(c[:-3]) # take all the list except the last 3 elements
print(a[:])# take all the list elements
a[3] = 20 # here we change the fourth element is the list
c[2:5] = [] #here we remove elements from the list
print(c)
b[:] = [] #remove all the elements in the list
d = [1,2,3,4]
e = [5,6,7,8]
f = [9,10,11,12]
g = [d,e,f]
print(g[0][3]) #print the fourth element in the fitst list
del c[3] # delete the element with index 3 in the c list
print(c)
c.remove(10) # remove the element in list c with the value 10 (the first one only)
print(c)
# you can marje two lists by add them (both should be lists)
h = ['ahmed' , 'ali' , 'sami' , 'youssef']
i = [1 , 2 , 3 , 4]
j = h+i
print(j)
l = j*3
print(l) #repeat the list three times
m = [0.0]*100 #create list with 100 elemnets with the value 0.0
print(m)
n = [[0]*8]*10 #here we create a matrix with 8 column and 10 rows
print(n)
print(len(a)) # what is the list length (look only at the number of rows)
print(sum(c)) #the sum of all the elements in the list c
print(min(c)) # what is the smallest element in the list c
print(max(c)) # what is the bigest element in the list c
# this is works with lists with the same type (only strings or only numbers)

print(sorted(c)) #sort the list element from the smaller to the biger even if it has number and strings in the same time
# in the sorted function the output will not be saved in the orignal list
# in the sort function the orignal list will changed to the new one
# this is the same with the letters 
c.sort()
print(c)











