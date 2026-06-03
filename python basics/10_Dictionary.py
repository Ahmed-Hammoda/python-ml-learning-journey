# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 03:08:52 2026

@author: ahmed hamouda
"""

# Define a dictionary of country codes
newdictionary = {'USA':'001', 'UK':'0044', 'Egypt':'002', 'KSA':'00699', 'UAE':'00971'}
# Note: If the first element was a string, all keys should follow the same type (for consistency)

# Define dictionaries of degrees (name -> value)
grades = {'ahmed': 78, 'aymen': 62, 'sami': 55, 'youssef': 89, 'mona': 82}
grades2 = {'ali': 71, 'sara': 45, 'yassine': 66, 'hamada': 38, 'mariam': 92}

# Dictionary comprehension: create a dictionary where key = n and value = n squared
a = {n: n**2 for n in range(6)}
print(a)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print(grades)

# Edit or add a key-value pair
grades['ahmed'] = 50  # Updates value of 'ahmed' to 50
print(grades)

# Check if a key exists in the dictionary
print('ahmed' in grades)  # True

# Get the value associated with a key
print(grades.get('ahmed'))  # 50

# Using get with default value: returns 40 if key does not exist
print(grades.get('nonexistent_key', 40))  # 40

# Delete a key-value pair
del(grades['ahmed'])
print(grades)

# Remove all elements from the dictionary
grades.clear()
print(grades)  # Output: {}

# Delete the dictionary variable completely
del(grades)
# print(grades)  # Would give an error: 'degrees' is no longer defined

# Copy a dictionary to a new variable
newdegrees = grades2.copy()  
# Changes to newdegrees will not affect the original degrees2 dictionary
# Create a set of keys
set1 = {'a', 'b', 'c', 'd'}

# Create a dictionary using the set as keys; all values default to None
dec = dict.fromkeys(set1)
print(dec)  # Output: {'a': None, 'b': None, 'c': None, 'd': None}

# Assign values to each key in the dictionary
dec['a'] = 80
dec['b'] = 52
dec['c'] = 12
dec['d'] = 59

# Print the updated dictionary with values
print(dec)  # Output: {'a': 80, 'b': 52, 'c': 12, 'd': 59}

# Get all the keys (names) from the dictionary and convert to a list
allnames = list(grades2.keys())
# Get all the values (grades) from the dictionary and convert to a list
allgrades = list(grades2.values())
# Get all the keys and values
allitems = list(grades2.items())

print(allnames)
print(allgrades)
print(allitems)

#we can assign more than one value for the same key but all values should follow the same type and number
grades = {'ahmed' : ('46','23','palestine'),'george' : ('36','20','egypt')} 
print(grades['ahmed']) #to get the data about ahmed
print(grades['ahmed'][1]) #to get only ahmed age



