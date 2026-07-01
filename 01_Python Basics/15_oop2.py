# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 01:26:07 2026

@author: ahmed hamouda
"""
# First example: using the class directly, not objects
class Car:
    # This is a class attribute
    color = 'red'


# Here you are NOT creating objects
# volvo and nissan are just another names for the class Car
volvo = Car
nissan = Car

# This changes the class attribute color to green
volvo.color = "green"

# This changes the same class attribute color to black
nissan.color = "black"

# Both will print black because volvo and nissan point to the same class
print(volvo.color)
print(nissan.color)


print("#########################################################")


# Second example: using real objects
class Car1:
    # __init__ runs automatically when we create a new object
    # self means "this object"
    def __init__(self, color):
        # Each object will have its own color
        self.color = color


# Create a new object with color green
volvo = Car1("green")

# Create another object with color black
nissan = Car1("black")

# Now each object has its own separate color
print(volvo.color)
print(nissan.color)


print("#########################################################")


# self separates the object values
class calc:
    def __init__(self, p2, p3):
        # self.power2 belongs to this object
        self.power2 = p2 ** 2

        # self.power3 belongs to this object
        self.power3 = p3 ** 3


# Create object a from calc
# p2 = 40
# p3 = 50
a = calc(40, 50)

# Print 40 squared = 1600
print(a.power2)

# Print 50 cubed = 125000
print(a.power3)


print("#########################################################")


class calc1:
    # Here p2 and p3 have default values
    # If the user does not give values, Python uses p2=10 and p3=20
    def __init__(self, p2=10, p3=20):
        self.power2 = p2 ** 2
        self.power3 = p3 ** 3


# Create object without giving p2 or p3
# Python will use the default values
a = calc1()

# 10 squared = 100
print(a.power2)

# 20 cubed = 8000
print(a.power3)


print("#########################################################")


class d:
    # nn is required
    # p2 has default value 10
    # p3 has default value 100
    def __init__(self, nn, p2=10, p3=100):
        self.power2 = p2 ** 2
        self.power3 = p3 ** 3

        # Store nn inside the object
        self.roots = nn

    # This is a method
    # A method is a function inside a class
    def root(self):
        # Print square root of self.roots
        print(self.roots ** 0.5)


# Create object a
# nn = 2500
# p2 = 10 default
# p3 = 100 default
a = d(2500)

# Call the root method
# square root of 2500 = 50
a.root()






