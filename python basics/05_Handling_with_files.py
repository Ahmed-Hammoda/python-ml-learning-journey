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
#OS library
#####################################################################
import os  # Import the OS module to work with file system paths

# Create nested directories (folders). If they already exist, do nothing because exist_ok=True
a = os.makedirs(
    r'C:\Users\hamou\Desktop\ME\AI\My-journey-in-Python\python basics\Files in python (for file 06)\test3',
    exist_ok=True
)
# check if the file exists or not
a = os.path.exists('C:\\Users\\hamou\\Desktop\\ME\\AI\\My-journey-in-Python\\python basics\\Files in python (for file 06)\\test3')
print(a)
#####################################################################
# shutil library – used for high-level file operations like copy
#####################################################################
import shutil as sh  # Import shutil and give it the alias 'sh'

# Copy a single file from source to destination
# copyfile(src, dst) copies the content only; destination file is overwritten if it exists
sh.copyfile(
    r'C:\Users\hamou\Desktop\ME\AI\My-journey-in-Python\python basics\Files in python (for file 06)\test.txt',
    r'C:\Users\hamou\Desktop\ME\AI\My-journey-in-Python\python basics\Files in python (for file 06)\test3.txt'
)

# Copy an entire directory tree (folder and all its contents) to a new location
# copytree(src, dst) copies the source directory to destination; destination must not exist
sh.copytree(
    r'C:\Users\hamou\Desktop\ME\AI\My-journey-in-Python\python basics\Files in python (for file 06)\test3',
    r'C:\Users\hamou\Desktop\ME\AI\My-journey-in-Python\python basics\Files in python (for file 06)\test4'
)
# Move a file from source to destination
# If the destination folder exists, the file is moved and renamed if needed
# The original file at the source path is removed after moving
sh.move('C:\\Users\\hamou\\Desktop\\ME\\AI\\My-journey-in-Python\\python basics\\Files in python (for file 06)\\test.txt',
        'C:\\Users\\hamou\\Desktop\\ME\\AI\\My-journey-in-Python\\python basics\\Files in python (for file 06)\\test3\\test55.txt')















