#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:58:11 2020

@author: rafliano
"""

import matplotlib.pyplot as plt
import numpy as np

# Scatter Plot
x1 = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y1 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Random Data Distributions
x2 = np.random.normal(5.0, 1.0, 1000)
y2 = np.random.normal(10.0, 2.0, 1000)

# plt.scatter(x1, y1)
plt.scatter(x2, y2)
plt.show()