# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:43:56 2026

@author: ahmed hamouda
"""

# Function to print stars
def star():
    for i in range(10):
        print('**')   

star()  # Call the function

###########################################

# Function to calculate average of two numbers
# In `find_avg()`, using '+' to concatenate string and number causes TypeError,
# which was fixed here by using ',' in print.
def find_avg(a, b):
    avgr = (a + b) / 2
    print('average is: ', avgr)  

find_avg(5, 6)
# Functions can accept different types of inputs: numbers, lists, dictionaries, etc.,
# but operations inside the function must be compatible with those types.

###########################################

def find_avg(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print('avgerage is ',sum/(len(numbers)))
    print(numbers)
    
find_avg(1,2,3,4,5,6,7)

###########################################

def test_var_args(f_arg,*argv):
    print('first normal arg: ',f_arg)
    for arg in argv:
        print("anther arg through *arvg :",arg)
        
test_var_args('ahmed', 'mohamed' , 'ali' , 'samy')

###########################################




