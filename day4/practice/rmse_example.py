import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error
import math

data = {
    "experience" : [1,2,3,4,5],
    # "salary" : [30000,40000,50000,60000,70000]
    # Practical
    "salary" : [30000,40000,50000,60000,100000]
}

df = pd.DataFrame(data)

X = df[["experience"]]
y = df["salary"]

model = LinearRegression()

model.fit(X,y)

predictions = model.predict(X)

mae = mean_absolute_error(y,predictions)

mse = mean_squared_error(y,predictions)

rmse = math.sqrt(mse)

print("Predictions")
print(predictions)

# Practical
print("MAE:")
print(mae)

print("MSE:")
print(mse)

print("RMSE:")
print(rmse)

# End Of Topic 3
# Theory Questions
# What is RMSE?
# Root Mean Squared Error, It converts squared error back to the original unit.
# Why do we calculate square root of MSE?
# To bring the error back to the original unit and make interpretation easier.
# Difference between MSE and RMSE?
# MSE - Average squared error.
# RMSE - Square root of MSE.
# Which metric is easier to interpret for business users?
# RMSE