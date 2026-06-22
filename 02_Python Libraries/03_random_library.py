# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:27:15 2026

@author: ahmed hamouda
"""

from random import *  # Imports all functions from the random module
# ⚠️ Note: Using '*' is not recommended better to import only what you need or use 'import random' but i use it for learning only

# Generate a random floating-point number between 0 (inclusive) and 1 (exclusive)
print(random())  # Example output: 0.6374

# Generate a random integer between 1 and 20 (both inclusive)
print(randint(1, 20))  # Example output: 13

# Generate a random floating-point number between 1 and 20
print(uniform(1, 20))  # Example output: 7.489

# Generate a random integer from 0 up to (but not including) 150
print(randrange(150))  # Example output: 42

# randrange(start, stop, step): returns a random integer in the range [start, stop) with a given step
print(randrange(0, 20, 2))  
# Example output: 0, 2, 4, ..., 18 (only even numbers)

# sample(population, k): returns k unique elements chosen randomly from the population
print(sample(range(200), 10))  
# Example output: [5, 123, 87, 45, 12, 199, 33, 77, 144, 8] (10 unique random numbers)

# shuffle(list): randomly reorders the elements of a list in place
items = [1, 2, 3, 4, 5, 6, 7, 8]
shuffle(items)
print(items)  
# Example output: [3, 7, 1, 6, 2, 4, 8, 5] (the order changes every time)

