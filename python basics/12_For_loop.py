# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 05:57:40 2026

@author: ahmed hamouda
"""

# Simple for loop using range()
for k in range(20):          # k takes values from 0 to 19
    print(k)                 # print each number
print('end')                 # always runs after the loop

# Nested loops with list comprehension
f = [(x, y) for x in range(10) for y in range(10)]  
# Creates all pairs (x, y) where x and y go from 0 to 9
print(f)

# Nested loops with a condition
f2 = [(x, y) for x in range(10) for y in range(10) if x > y]  
# Only include pairs where x > y
print(f2)

# Looping over a string by index
a = 'hello python how are you doing'
z = ''

for l in range(len(a)):      # l goes from 0 to length of string - 1
    print(a[l])              # prints each character individually
    
print('-----------------')

# Reverse a string using a for loop
for l in range(len(a)):
    z = z + a[len(a) - l - 1]  # take characters from the end to start
print(z)

# Looping over each character in a string
b = 'supercalifragilisticexpialidocious'

for v in b:
    if v == 'x':              # skip the character 'x'
        continue              # continue to next iteration
    print(v)
    
print('-----------------')

for v in b:
    if v == 'x':              # stop the loop if character 'x' is found
        break
    print(v)
    
print('-----------------')

# Loop with condition to skip numbers divisible by 3 or 5
for c in range(20):
    if c % 5 == 0 or c % 3 == 0:
        continue              # skip this iteration
    print(c)
    
print('-----------------')

# Looping over a list
students = ["ahmed", "ramy", "heba"]

for d in students:
    print(d)
    
print('-----------------')

# Looping over dictionary keys
grades = {'ahmed': 35, 'aymen': 40, 'sami': 50}

for i in grades.keys():
    print(i)                 # prints only the keys
    
print('-----------------')

# Using enumerate to get index and value
for i, v in enumerate(['tic','tac','toe']):
    print(i, ':', v)
    
print('-----------------')

# Looping over two lists at the same time using zip
students = ['samy','mona','ramy','ahmed']
grades = [25,33,66,95]

for i, a in zip(students, grades):
    print('student ' + i + ' got ' + str(a) + ' degree')
    
print('-----------------')

# List using condition and for loop
v = [i for i in range(200) if i % 5 == 0]  
# Create a list of numbers from 0 to 199 that are divisible by 5
print(v)

print('-----------------')

m = [(i,j) for i in range(2) for j in range(3)]
print(m)

print('-----------------')

for x in range(20):
    print('more')
else:
    print('less')
    
print('-----------------')

print(sum([1.0/k for k in range(1,11)]))

print('-----------------')

print([r**2 for r in [10*i for i in range(10)]])



