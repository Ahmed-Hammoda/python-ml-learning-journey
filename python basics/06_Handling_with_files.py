# -*- coding: utf-8 -*-
"""
reated on Sat May 28 16:55:12 2026

@author: ahmed hamouda
"""
f = open('C:\\Users\\hamou\\Desktop\\ME\\AI\\My-journey-in-Python\\python basics\\Files in python (for file 06)\\test.txt','w')
# if the file is not exist python will create it
f.write('write this line in the file') # remove any thing in the file and write the new string
f.close()
# to add on the file we replace the w with a (append)
f = open('C:\\Users\\hamou\\Desktop\\ME\\AI\\My-journey-in-Python\\python basics\\Files in python (for file 06)\\test.txt','a')
f.write('\nnew line to append')
f.close()
#to read a file
f = open('C:\\Users\\hamou\\Desktop\\ME\\AI\\My-journey-in-Python\\python basics\\Files in python (for file 06)\\test.txt','r')
for a in f :
    print(a)
f.close()
# to write on a csv file
f = open('C:\\Users\\hamou\\Desktop\\ME\\AI\\My-journey-in-Python\\python basics\\Files in python (for file 06)\\test2.csv','w')
f.write('new line1')
f.write('\nnew line2')
f.write('\nnew line3')
f.write('\nnew line4')
f.close()
# to read from csv
f = open('C:\\Users\\hamou\\Desktop\\ME\\AI\\My-journey-in-Python\\python basics\\Files in python (for file 06)\\test2.csv','r')
for a in f :
    print(a)
f.close()

#####################################################################

#####################################################################
import os  # Import the OS module to work with file system paths

# Create nested directories (folders). If they already exist, do nothing because exist_ok=True
a = os.makedirs(
    r'C:\Users\hamou\Desktop\ME\AI\My-journey-in-Python\python basics\Files in python (for file 06)\test3.txt',
    exist_ok=True
)