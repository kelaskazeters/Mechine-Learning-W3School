#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:25:31 2020

@author: rafliano
"""

import matplotlib.pyplot as plt
from scipy import stats

# Bad Fit
x1 = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y1 = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x1, y1)

def myfunc(x1):
  return slope * x1 + intercept

mymodel = list(map(myfunc, x1))

plt.scatter(x1, y1)
plt.plot(x1, mymodel)
plt.show()

# Very Low R-Squared Value
print(r)