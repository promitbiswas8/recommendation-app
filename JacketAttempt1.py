#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 14:06:52 2020

@author: promit
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Attemp1.0.csv')
z = dataset.iloc[:, 0].values
x = dataset.iloc[:, 0:2].values
y = dataset.iloc[:, 2].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
labelencoder_y = LabelEncoder()
labelencoder_z = LabelEncoder()
onehotencoder = OneHotEncoder()
z = labelencoder_z.fit_transform(z)
x[:, 0] = labelencoder_x.fit_transform(x[:, 0])
x[:, 0:1] = labelencoder_x.fit_transform(x[:, 0:1])
x[:, 1] = labelencoder_x.transform(x[:, 1])
x[:, 2] = labelencoder_x.transform(x[:, 2])
x[:, 0] = labelencoder_x.fit_transform(x[:, 0])
onehotencoder = OneHotEncoder()
y.reshape(1,-1)
x = onehotencoder.fit_transform(x).toarray()

y = onehotencoder.fit_transform(y).toarray()
y = labelencoder_y.fit_transform(y)


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

y_train = y_train.reshape(-1,1)
y_test.reshape(1,-1)


from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)

from sklearn.linear_model import LinearRegression 
lin_reg = LinearRegression()
lin_reg.fit(x, y)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(x)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)


