import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error

data = {
    "experience" : [1,2,3,4,5],
    "salary" : [30000,40000,50000,60000,70000]
}

df = pd.DataFrame(data)

X = df[["experience"]]
y = df["salary"]

model = LinearRegression()

model.fit(X,y)

predictions = model.predict(X)

mse = mean_squared_error(y,predictions)

print("MSE:")
print(mse)

# Theory Questions
# What is MSE?
# Mean Squared Error, which is an metric used to measure model quality.
# Why do we square errors in MSE?
# To punish big mistakes more heavily.
# Difference between MAE and MSE?
# MAE - Average Prediction Mistake (Mean Absolute Error)
# MSE - Mean Squared Error
# MAE averages the errors, MSE squares each error and then averages it. 
# Which metric punishes large mistakes more?
# MSE - Mean Squared Error.

# Practical Questions
# Change salary
# 70000 -> 100000
y = [30000,40000,50000,60000,100000]
# and rerun.
# Observe whether MSE changes.
# Print both
prediction = model.predict(X)
print("Predictions:")
print(prediction)
print("MAE:")
print(mean_absolute_error(y,prediction))
print("MSE:")
print(mean_squared_error(y,prediction))