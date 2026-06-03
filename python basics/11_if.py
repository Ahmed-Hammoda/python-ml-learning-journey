# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 05:08:41 2026

@author: ahmed hamouda
"""
#################################################
# if statement
#################################################

x = 5

# if statement: executes the indented code only if the condition is True
if x == 5:  # Check if x is equal to 5
    print(x)      # This line is executed because x == 5
    print(3 * x)  # Indented lines under 'if' belong to the if-block

# This line is NOT indented, so it always runs regardless of the if condition
print(x * 5)  # Always prints 25

# Another if statement
if x == 3:  # Check if x is equal to 3
    print(x)      # Not executed because x is 5
    print(3 * x)  # Not executed

# Again, this line is outside the if-block and always runs
print(x * 5)  # Always prints 25

#################################################
# if else statement
#################################################

y = 17

# if statement: check a condition
if y > 5:        # If y is greater than 5
    print('yes')  # This line runs because y = 17 > 5
else:             # If the condition above is False
    print('no')   # This line would run if y <= 5

# This line is outside the if else block and always runs
print('none')     # Always prints 'none'

#################################################
# elif statement (used to check multiple conditions)
#################################################

grade = 4

# Check multiple conditions using if, elif, and else
if grade < 5:          # First condition: if grade is less than 5
    print('fall')      # This line runs because grade = 4 < 5
elif grade < 7:        # Second condition: checked only if previous condition was False
    print('medium')    
elif grade < 10:       # Third condition: checked only if all previous conditions were False
    print('good')
else:                  # If none of the above conditions are True
    print('other')

# This line is outside the if-elif-else block always runs
print('hello')


#another way to write the if-else

a=5
b=8

maximum = a if (a>b) else b

print(maximum)






