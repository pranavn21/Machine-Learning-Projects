# -*- coding: utf-8 -*-
"""part2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IwEGsJUKstb0SIdltNcqo6Hx0h_UeoSc
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

df = pd.read_csv("https://raw.githubusercontent.com/pranavn21/real-estate/main/Real%20estate%20valuation%20data%20set.csv")
df_part = df[["X2 house age", "Y house price of unit area"]]

df.head()

X = df_part["X2 house age"]
Y = df_part["Y house price of unit area"]
# Continue from here

plt.scatter(X,Y)

X = np.expand_dims(X,1) # Making sure that the dimensions are expanded
x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.2)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
MSE = mean_squared_error(y_test, y_pred)
variance = model.score(x_test,y_test) # Variance
rSquared = variance**2

print("Model score:\t", model.score(x_test, y_test))
print("MSE:\t\t", MSE)
print("Variance:\t",variance)
print("r^2:\t\t",rSquared)
