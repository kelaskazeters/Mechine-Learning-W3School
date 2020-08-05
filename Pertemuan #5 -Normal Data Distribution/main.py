#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:53:57 2020

@author: rafliano
"""

import numpy as np
import matplotlib.pyplot as plt

# Normal Data Distribution
x1 = np.random.normal(5.0, 1.0, 100000)

plt.hist(x1, 100)
plt.show()