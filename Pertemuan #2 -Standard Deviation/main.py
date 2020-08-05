#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 14:45:14 2020

@author: rafliano
"""

import numpy as np

speed1 = [86,87,88,86,87,85,86]
speed2 = [32,111,138,28,59,77,97]

# Standard Deviation
x1 = np.std(speed1)
x2 = np.std(speed2)

# Variance
x3 = np.var(speed2)

print(x3)