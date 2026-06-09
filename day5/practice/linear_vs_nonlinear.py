import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# DataSet 1 - Linear
linear_data = {
    "experience" : [1,2,3,4,5,6],
    "salary" : [30000,40000,50000,60000,70000,80000]
}

linear_df = pd.DataFrame(linear_data)

model = LinearRegression()
model.fit(linear_df[["experience"]],linear_df["salary"])
pred = model.predict(linear_df[["experience"]])

plt.scatter(linear_df["experience"],linear_df["salary"])
plt.plot(linear_df["experience"],pred)
plt.title("Linear Relationship")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()

# Dataset 2 - Non-Linear
non_linear_data = {
    "experience" : [1,2,3,4,5,6],
    "salary" : [30000,45000,90000,85000,120000,50000]
}

non_linear_df = pd.DataFrame(non_linear_data)

model = LinearRegression()
model.fit(non_linear_df[["experience"]],non_linear_df["salary"])
pred = model.predict(non_linear_df[["experience"]])

plt.scatter(non_linear_df["experience"],non_linear_df["salary"])
plt.plot(non_linear_df["experience"],pred)
plt.title("Non-Linear Relationship")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()

# Theory Questions
# What is a linear relationship?
# A linear relationship is one where the feature and label follow an approximately straight-line trend.
# Does Linear Regression require perfectly straight data?
# No, Prediction may not be as accurate because the data does not closely follow a straight-line trend.
# Why does Linear Regression perform better on linear data?
# Linear Regression tries to learn One Best Fitting Straight Line if the data already follows a straight line, then Best fitting line ~ Actual data . So naturally predictions become better.
# Can Linear Regression still be used on slightly irregular data?
# Yes. If the data is only slightly irregular, Linear Regression can still produce reasonably good predictions. Whether it is acceptable depends on business requirements.