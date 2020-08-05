#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 20:03:06 2020

@author: rafliano
"""

import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")

# Multiple Regression
X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)


#predict the CO2 emission of a car where the weight is 2300g, and the volume is 1300ccm:
predictedCO2 = regr.predict([[3300, 1300]])

print(predictedCO2)

# Coefficient
print(regr.coef_)