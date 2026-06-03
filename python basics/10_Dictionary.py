# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 03:08:52 2026

@author: ahmed hamouda
"""

# Define a dictionary of country codes
newdictionary = {'USA':'001', 'UK':'0044', 'Egypt':'002', 'KSA':'00699', 'UAE':'00971'}
# Note: If the first element was a string, all keys should follow the same type (for consistency)

# Define dictionaries of degrees (name -> value)
degrees = {'ahmed': 21, 'aymen': 35, 'sami': 55, 'youssef': 15, 'mona': 50}
degrees2 = {'ahmed': 21, 'aymen': 35, 'sami': 55, 'youssef': 15, 'mona': 50}

# Dictionary comprehension: create a dictionary where key = n and value = n squared
a = {n: n**2 for n in range(6)}
print(a)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print(degrees)

# Edit or add a key-value pair
degrees['ahmed'] = 50  # Updates value of 'ahmed' to 50
print(degrees)

# Check if a key exists in the dictionary
print('ahmed' in degrees)  # True

# Get the value associated with a key
print(degrees.get('ahmed'))  # 50

# Using get with default value: returns 40 if key does not exist
print(degrees.get('nonexistent_key', 40))  # 40

# Delete a key-value pair
del(degrees['ahmed'])
print(degrees)

# Remove all elements from the dictionary
degrees.clear()
print(degrees)  # Output: {}

# Delete the dictionary variable completely
del(degrees)
# print(degrees)  # Would give an error: 'degrees' is no longer defined

# Copy a dictionary to a new variable
newdegrees = degrees2.copy()  
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







