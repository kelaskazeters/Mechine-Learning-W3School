#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:33:39 2020

@author: rafliano
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Polynomial Regression
x1 = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y1 = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = np.poly1d(np.polyfit(x1, y1, 3))

# Predict Future Values
speed = mymodel(17)
print(speed)

myline = np.linspace(1, 22, 100)

plt.scatter(x1, y1)
plt.plot(myline, mymodel(myline))
plt.show()

# R-Squared
print(r2_score(y1, mymodel(x1)))
