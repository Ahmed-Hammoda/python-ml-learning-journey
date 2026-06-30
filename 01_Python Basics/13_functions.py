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

print("###########################################")

# Function to calculate average of two numbers
# In `find_avg()`, using '+' to concatenate string and number causes TypeError,
# which was fixed here by using ',' in print.
def find_avg(a, b):
    avgr = (a + b) / 2
    print('average is: ', avgr)  

find_avg(5, 6)
# Functions can accept different types of inputs: numbers, lists, dictionaries, etc.,
# but operations inside the function must be compatible with those types.

print("###########################################")

def find_avg(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print('avgerage is ',sum/(len(numbers)))
    print(numbers)
    
find_avg(1,2,3,4,5,6,7)

print("###########################################")

def test_var_args(f_arg,*argv):
    print('first normal arg: ',f_arg)
    for arg in argv:
        print("anther arg through *arvg :",arg)
        
test_var_args('ahmed', 'mohamed' , 'ali' , 'samy')

print("###########################################")

# **values means the function can receive many keyword arguments
# Example: one=1, two=2, three=3
# Python will store them inside a dictionary called values
def print_values(**values):

    # Loop through each key and value inside the dictionary
    # key = the name, like "one"
    # value = the number, like 1
    for key, value in values.items():

        # Print the key and value in this format: key = value
        print("{} = {}".format(key, value))

print_values(one=1, two=2, three=3)

print("###########################################")

def avg_of_two(a,b):
    print((a+b)/2)
    
var1 = {"a" : 3 , "b" : 5} # dictionary
# the ** is to tell the function to deal with the var1 as a dictionary
avg_of_two(**var1) 

print("###########################################")

# *args is used to collect extra positional arguments
# It stores them in a tuple, not a list

# **kwargs is used to collect extra keyword arguments
# It stores them in a dictionary

def show_details(a, b, *args, **kwargs):

    print("a : ", a)
    print("b : ", b)
    print("*args : ", args)
    print("**kwargs : ", kwargs)


# Here:
# a = 10
# b = 5
# args = (2, 5, 8, 12, 25)
# kwargs = {}
show_details(10, 5, 2, 5, 8, 12, 25)

# Here:
# a = 55
# b = 45
# args = (3, 5, 8, 88, 62)
# kwargs = {"c": 1, "d": 2, "e": 3}
show_details(55, 45, 3, 5, 8, 88, 62, c=1, d=2, e=3)

print("###########################################")

def test_args_kwargs(arg1,arg2,arg3):
    print("arg1 : ",arg1)
    print("arg2 : ",arg2)
    print("arg3 : ",arg3)

args = ('two',5,7)
test_args_kwargs(*args)
print('---------------')
kwargs = {"arg3":55,"arg2":22,"arg1":'hello'}
test_args_kwargs(**kwargs)

print("###########################################")

# the n=2 is a inital value for the n so in we write power(3) the m=3 and the n=2 (by default)
def power(m , n = 2):
    print(m**n)
    
power(4)
power(4,3) #here we change the n to 3
power(n=3,m=2) # we mention the var name so we can change the parameters order
# we can use this in the phone number applications where the default is the country start number and we can change it

print("###########################################")

def parrot(voltage, state='a stiff', action='voom'):
    print ("-- This parrot wouldn't", action),
    print ("if you put", voltage, "volts through it."),
    print ("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM "}

parrot(**d) # the function will take the dictionary and full the function parameters

print("###########################################")

ff=5
def aa():
    global ff # to make the ff var a global var so no scope limits
    ff = 11

print(ff)
aa()
print(ff)

print("###########################################")

# lambda is a short way to write a function
power = lambda x,y : x**y

print(power(2,3))

print("###########################################")

# short way to write different functions in the same line using lambda 
power = [lambda x : 1,lambda x : x,lambda x:x**2,lambda x:x**3]

print(power[0](5)) #you call the function you need using the index
print(power[1](5))
print(power[2](5))
print(power[3](5))

print("###########################################")

mylist = (0,1,2,3,4,5,6,7,8,9)

#you can use the lambda to filter a list with the condition you want
evennumbers = list(filter(lambda x:x%2 == 0, mylist)) 
oddnumbers = list(filter(lambda x:x%2 != 0, mylist)) 

print(evennumbers)
print(oddnumbers)

print("###########################################")

mylist = (0,1,2,3,4,5,6,7,8,9)

# map function take each element from the list and apply a function on it
print("square list" , list(map(lambda x:x**2, mylist)))

list1 = (1,2,3,4,5)

def cpower(x):
    return x**3

print(list(map(lambda x:cpower(x), list1))) #another way to use the map

print("###########################################")

# Define a generator function called yie
def yie():

    for i in range(10):
        # yield returns one value at a time
        # It pauses the function here and remembers where it stopped
        yield i

# Call the generator function
# f is now a generator object
f = yie()

# next(f) takes the first value from the generator
# i = 0
print(next(f))

# next(f) continues from where it stopped
# i = 1
print(next(f))

# next(f) continues again
# i = 2
print(next(f))

print("###########################################")

def fibon(n):
    # Give a and b the value 1
    a = b = 1
    result = []

    for i in range(n):
        # Add the current value of a to the list
        result.append(a)      
        # Update a and b
        # a becomes the old b
        # b becomes old a + old b
        a, b = b, a + b  
    return result

print(fibon(20))

print("###########################################")


# Example: 5! = 5 * 4 * 3 * 2 * 1
def fac(n):

    # Base case
    # If n is 1, stop the recursion and return 1
    if n == 1:
        return 1

    # Recursive case
    # n * fac(n - 1)
    # The function calls itself with a smaller number
    else:
        return n * fac(n - 1)


print(fac(5))












































