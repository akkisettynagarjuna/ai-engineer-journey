import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

data = {
    "experience" : [1,2,3,4,5],
    "salary" : [30000,40000,50000,60000,70000]
}

df = pd.DataFrame(data)

# Features
X = df[["experience"]]
# Label
y = df["salary"]

# Model - Created Empty Linear Regression Model
model = LinearRegression()

# Training the Model
model.fit(X,y)

# This time no train/test split because focus is visualization intuition only not evaluation currently.

# Predictions
predicted_salary = model.predict(X) # Now machine predicts salary for ALL dataset points. These predictions form regression line.

# Visualization
# Actual Data Points
plt.scatter(X,y)
# Regression line
plt.plot(X, predicted_salary)

plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")

plt.show()

# Questions I have
# Why this plt.scatter(X,y)?
# plt.scatter(X,y) draws actual dataset points.
#
# These points represent the real observations
# provided to the machine.
#
# We draw them so that we can visually compare:
# actual data points
# vs
# machine learned regression line.

# THEORY QUESTIONS
# What do scatter points represent?
# Scatter points represents the actual dataset values.
# What does regression line represent?
# Regression line represents machine learned relationship between input and output variables.
# Why line called “best fitting line”?
# Best fitting line means the line that represents the overall trend of the data with minimum prediction error.
# Why Linear Regression called linear?
# Linear Regression is called linear because it learns a straight-line relationship between variables.
# What does model.predict(X) generate here?
# model.predict(X) generates predicted outputs using the learned pattrens.
# Why visualization useful in ML?
# Visualization helps us understand:
# data patterns
# trends
# relationships
# and model behavior visually.

# MINI THEORY QUESTION

# Let's test intuition.

# Suppose graph looks like:

# *
#         *
#   *
#               *
#       *

# Points are scattered randomly.

# Question:

# Will Linear Regression work well here?
# Why or why not?

# Answer in your own words.

# To be frank I can't tell here it works well or not, but I would say Linear regression tries to draw the straight line that covers max dataset points.