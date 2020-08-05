#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:04:06 2020

@author: rafliano
"""

import matplotlib.pyplot as plt
from scipy import stats

# Linear Regression
x1 = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y1 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x1, y1)

def myfunc(x1):
  return slope * x1 + intercept

# Predict Future Values
speed = myfunc(10)

mymodel = list(map(myfunc, x1))

plt.scatter(x1, y1)
plt.plot(x1, mymodel)
plt.show()
print(speed)

# R-Squared
print(r)
