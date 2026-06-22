# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:09:11 2026

@author: ahmed hamouda
"""

import statistics as st  # Import the statistics module for common statistical calculations

a = [1, 2, 3, 4, 5, 6]

# Mean (arithmetic average)
# Law: Mean = sum of all values / number of values
print(st.mean(a))  

# Harmonic mean (useful for rates)
# Law: Harmonic mean = n / sum(1/x_i) for i=1..n
print(st.harmonic_mean(a))  

# Median (middle value)
# Law: 
# If odd count: take the middle value after ordering
# If even count: average the two middle values
print(st.median(a))  

# Median low: returns the lower of the two middle values (if even)
print(st.median_low(a)) 

# Median high: returns the higher of the two middle values (if even)
print(st.median_high(a)) 

###################################################################

b = [2, 4, 8, 8, 3, 2, 1, 8, 6, 7, 8]

# Mode: most frequently occurring value
# Law: Mode = value that appears most often
print(st.mode(b))  # Output: 8

# Standard deviation: measure of spread/variability
# Law: Stdev = sqrt(sum((x_i - mean)^2)/(n-1))
# Explanation: Higher stdev = more spread in the data
# Example: if 3 classes have grades the class with the most variety will have the highest stdev
print(st.stdev(b))  

# Variance: square of standard deviation, measures dispersion
# Law: Variance = average of squared differences from the mean
print(st.variance(b))  