# Required Imports
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Required Data
data = {
    "experience" : [1,2,3,4,5,6,7,8],
    "age" : [22,24,26,28,30,32,34,36],
    "salary" : [30000,40000,50000,60000,70000,80000,90000,100000]
}

# Pandas DataFrame for the given data
df = pd.DataFrame(data)

# Features
X = df[["experience","age"]]

# Label
y = df["salary"]

# Train,Test split of data
X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42
)

# Empty Model
model = LinearRegression()

# Training model using fit()
model.fit(X_train,y_train)

# Predict on X_test using trainned model
X_test_df = pd.DataFrame(X_test)
prediction_on_X_test = model.predict(X_test_df)
print(X_test_df)
print(prediction_on_X_test)

# MAE Calculation between actual and know ones
average_prediction_error = mean_absolute_error(y_test,prediction_on_X_test)
print(round(average_prediction_error,2))

# Predict salary for a new employee : experience = 10 , age = 40
new_emp_data = {
    "experience" : [10] ,
    "age" : [40]
}
new_emp_df = pd.DataFrame(new_emp_data)
print(model.predict(new_emp_df))