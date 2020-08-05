#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:17:18 2020

@author: rafliano
"""

import numpy as np
import matplotlib.pyplot as plt

# Membuat Histogram
x1 = np.random.uniform(0.0, 5.0, 250)

# Big Data Distribution
x2 = np.random.uniform(0.0, 5.0, 100000)

plt.hist(x1, 5)
plt.hist(x2, 100)
plt.show()