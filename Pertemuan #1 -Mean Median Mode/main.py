#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 14:19:54 2020

@author: rafliano
"""

"""

Mean - The Average Value
Median - The Mid Point Value
Mode - The Most Common Value

"""

import numpy as np

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Mencari Rata-Rata Kecepatan
x1 = np.mean(speed)

# Mencari Angka Dengan Nilai Di Tengah-Tengah
x2 = np.median(speed)

# Mencari Angka Yang Umum
from scipy import stats

x3 = stats.mode(speed)

print(x3)