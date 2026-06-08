# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:27:36 2026

@author: ahmed hamouda
"""

n = int(input('input number : '))#take string input from the console then convert it to integer
while n <= 10:
    print(n)
    n = n+1
print('Done')


while True:
    a = int(input('Number ?'))
    if a > 15:
        print('yes')
        break
    else:
        print('no')
print('end')


a = 8
while a:
    print(a)
    a=a-1
    