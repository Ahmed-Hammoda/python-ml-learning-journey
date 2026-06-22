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
o = [1,2,3,4,5,6,7,8,9,10]
p = sorted(o , reverse=True) # to reverse the list
print(p)
q = 'I love python because it is an easy programming software'
r = q.split()
print(r) #the split will split in each sapce by defult and put each one as an element in the list
q = 'I,love,python,because,it,is,an,easy,programming,software'
r = q.split(sep= ',' , maxsplit=4) # i can control for what the split happend and how many times
print(r)
print(10 in o) # check if the 10 in the o list or not (true or false)
o.extend(a)
print(o) # add the list a to o and update o
s = c + a
print(s) # here i put list c and a in a new list but in the extend we change one of the lists
a.append(35) # add a new value to the list (in the last index)
print(a)
a.insert(3, 'aaa') # add the string aaa in the index 3 (the fourth elemen) in the list a
print(a)
u = [1,56,2,64,2,4,49,4,2,5]
print(u.count(2)) # how many times the element 2 exists in the list
print(u.index(2)) # where the first 2 appear in the list (give me the index)
u.reverse() #reverse the list order
print(u)
print(u.pop()) #remove the last element in the list
print(u.pop(3)) #remove the element with the index 3 in the list
t = list(range(20)) # to do a list with elements from 0 to 19
print(t)
t = list(range(3,20)) #from 3 to 19
print(t)
t = list(range(2,20,2)) # from 2 to 19 with a step = 2()
print(t)
y = [x**3 for x in range(12)] # form 0^3 to 11^3
print(y)
y = list(map(lambda x : x**5 , range(10))) # it works like the [x**3 for x in range(12)] concept
print(y)
listofjobs = [(names,jobs) for names in ['ahmed','mohamed','ali'] for jobs in ['engineer' , 'lawyer' , 'doctor']]
print(listofjobs) # this way is important in machine learning
combination = [(x,y,z) for x in range(10) for y in range(8) for z in range(6)] # do all the combinations for these numbers
print(combination)
x = iter([1,5,4,52,41,2,588,1,11,58])
print(next(x)) # always go to the next element until reatch the last one
print(next(x))
print(next(x))
print(next(x))
# i can use the range in the iter function
w = [2,88,5,5,6,6,165,4,81,9,9,7,4,6]
z = w # the w list will be saved in the z var
zz = w.copy()
w[5] = 100
print(z) # if you edit the w the z we also change
print(zz) # will not change becuse it takes only the old copy (no updates if the  w changed in the next lines)
names = ['a','b','c','d','e']
for c , value in enumerate(names , 1): #will give each va
    print(c , value)
countries = ['egypt','libia','jordan']
names = ['ahmed','mona','youssef']
for a,b in zip(names,countries):
    print(a + ' is living in '+b)
##########################################################################
# Import helper functions from the operator module.
#
# itemgetter(index)
#   - Returns a function that extracts one or more items from an object.
#   - Commonly used as a sorting key.
#
# methodcaller(method_name, *args)
#   - Returns a function that calls the specified method on an object.
#   - Useful when sorting based on the result of a method call.
##########################################################################
from operator import itemgetter
from operator import methodcaller

##########################################################################
# List of students represented as tuples:
# (name, country, age)
##########################################################################
students = [
    ('ahmed', 'egypt', 35),
    ('zakarya', 'yemen', 25),
    ('mona', 'syria', 19),
    ('mohamed', 'tunise', 21)
]

##########################################################################
# List of names that will be sorted according to the number of times
# the letter 'a' appears in each string.
##########################################################################
s = [
    'ahmed',
    'monaaaaaaaa',
    'ali',
    'mostafa',
    'abdelrahman'
]

##########################################################################
# Sort students by age (index 2 of each tuple).
#
# itemgetter(2) extracts the age from each tuple and uses it as
# the sorting key.
#
# Example:
# itemgetter(1, 2)
#   - Sort first by index 1 (country).
#   - If two countries are the same, sort by index 2 (age).
##########################################################################
sorted_students = sorted(students, key=itemgetter(2))

##########################################################################
# Sort strings by the number of occurrences of the letter 'a'.
#
# methodcaller('count', 'a') creates a function equivalent to:
# lambda x: x.count('a')
#
# Strings with fewer 'a' characters appear first.
##########################################################################
sorted_names = sorted(s, key=methodcaller('count', 'a'))

##########################################################################
# Display the sorted results.
##########################################################################
print("Students sorted by age:")
print(sorted_students)

print("\nNames sorted by the number of 'a' characters:")
print(sorted_names)












 


