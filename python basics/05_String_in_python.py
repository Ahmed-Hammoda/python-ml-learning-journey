# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:08:12 2026

@author: ahmed hamouda
"""
import numpy as np

# in here we will learn how to deal with strings in python
a = "hello i am ahmed"
b = '0123456789' # '' or "" can create a string
c = "hello,i,am,ahmed"
print(a[5]) #python deal with the space as a letter and the counting start from 0
print(a[-2]) #the second letter from the right
print(a*3) #repeat the string 3 times without space
print(a[2:8]) #take the letters form index 2 to 7 (not 8)
print(a[:10]) # that mean from index 0 to 9
print(b[4:9:2]) # that mean take from 4 to 8 and the step is 2 so take 4 and ignor 5 etc..
print(b[:7:3]) #start from index 0 and the step is 3
print(b[-1:4:-1]) #strat from 9 and walk 5 steps in reverse
# This slice returns an empty string because it starts at the last character (-1)
# but tries to move forward with step 1 toward index 4, which is before it.
print(b[-1:4:1])
print(b[::-1]) # get the string in reverse
print(list(a)) #get each letter alone
print(sorted(list(a))) # sort the letters and give each one alone in order from small to big
print(set(a)) #remove any repeated letter because its a set
print(a.split()) #split each word alone depend on the space
print(c.split(",")) # split when there is a ","
print(a.splitlines()) # Splits the string into a list of lines, separating at line breaks like \n
print(c.partition(",")) # partition on the first "," only
# we can use the partition in many examples like the get the first part from an email address
d = "ahmed@gmail@com"
print(d.rpartition("@")) # in here the search start from the right not the left (default)
print(d.find("com")) # give the index of the first letter from "com" in the string (serach starting from the left)
print(d.index("com")) # the different between find and index that if the string we try to find in not exist find will give -1 but index will give error
print(d.replace("c", "i")) # replace each c in the string with 
print(d.replace("com", "net")) # replace words
print(d.capitalize()) # the first letter is capital and the rest small
print(a.title()) # make the first letter from each word capital
print(d.upper()) # all letter are capital
print(d.swapcase()) # swap each letter if its capital make it samll and the opposite
print(d.center(30)) # make the string centered in 30 letter space 
print(a.ljust(30)) # complete to 30 letter with spaces from the left
print(a.rjust(30)) # complete to 30 letter with spaces from the right
print(a.rjust(30 , "*")) # complete to 30 letter with a * (add the * in the right)
print(b.zfill(20)) # complete to 20 letters with zeros (add them from the left)
print(a.isalpha()) # are all the latters in this string an alphabet latters (true or false) "space is not an alphabet latter"
print(a.strip()) # remove any space after the string
print(a.rstrip()) # remove any space after the string (from right)
print(a.lstrip()) # remove any space after the string (from left)
# strip and just are canceled each other
print("123", a ,"\n" ,a) # \n for a new line
e = r"C:\windows\new folder"
print(e) # we use the r before the string to ignore the \n and print it as it is
f = "my name is \t\t\tahmed"
print(f)
g = '''hi
hi
hi
hi
i am ahmed hamouda'''
print(g)
print(a, end= '') #print a and b without any space between
print(b)
h = 'ahmed'
i = "palestine"
k = 23
j = 'my name is %s and i am from %s and i am %05d years old' %(h,i,k) # %s for string and %d for numbers (%05d mean complete the number to 5 digits with 0)
# if i did not put the 05 and keep it %5d python will complete the number with empty spaces
print(j)
print('I \'wnant\' food') # use \' to add the '' as string
print(b.isdigit()) # is this string number or not
print(a.isupper()) #is all the letter in this string uppercase or not
print(a.islower()) #is all the letter in this string lowercase or not
print(a.istitle()) #is this string work as a title or not
print(a.startswith('hello')) # to check if the string start with any word you want
print(a.endswith('ahmed')) # to check if the string end with any word you want
l = '@@'.join(('ahmed','ali','sara')) # join the word inside the string with the @@ or any thing you want
print(l)
m = "the value of pi is {}".format(np.pi) # replace the {} with what is the format
print(m)
print("{0} and {1}".format('red', 'blue'))


