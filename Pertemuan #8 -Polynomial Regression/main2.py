#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 19:00:16 2020

@author: rafliano
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Bad Fit
x1 = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y1 = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = np.poly1d(np.polyfit(x1, y1, 3))

myline = np.linspace(2, 95, 100)

plt.scatter(x1, y1)
plt.plot(myline, mymodel(myline))
plt.show()

# Very Low R-Squared
print(r2_score(y1, mymodel(x1)))
