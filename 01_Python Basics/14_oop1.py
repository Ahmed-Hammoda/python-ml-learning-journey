# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 00:39:23 2026

@author: ahmed hamouda
"""

# Create a class called Car
# A class is like a blueprint/template for creating cars
class Car:

    # These are class attributes
    # They belong to the class Car
    length = 15
    width = 8
    height = 6
    color = "red"
    volume = length * width * height


# Access the volume directly from the class Car
print(Car.volume)

# Create a new object from the Car class
# volvo is now an object/instance of Car
volvo = Car()

# Access the color from the volvo object
# Python gets the color value from the Car class
print(volvo.color)

