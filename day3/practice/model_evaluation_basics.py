import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

data = {
    "experience" : [1,2,3,4,5],
    "salary" : [30000,40000,50000,60000,70000]
}

df = pd.DataFrame(data)

# Features
X = df[["experience"]]

# Labels
y = df["salary"]

# Train/Test Split
X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42
)

# Model
model = LinearRegression()

# Training
model.fit(X_train,y_train)

# Prediction
predictions = model.predict(X_test)

print("Predictions:")
print(predictions)

# Evaluation
mae = mean_absolute_error(y_test,predictions)
print("Mean Absolute Error:")
print(mae)

# THEORY QUESTIONS
# Why model evaluation needed?
# Model evaluation is needed to check how well the model predictions match actual answers. Smaller MAE generally means better predictions.
# What is Mean Absolute Error?
# Mean Absolute Error (MAE) calculates average prediction error between actual outputs and predicted outputs.
# Why smaller MAE better?
# It says the model is giving better predictions.
# What does mean_absolute_error() compare?
# mean_absolute_error() compares actual answers vs predictions
# Why prediction done on testing data?
# Prediction is done on testing data to check how well model performs on unseen data.
# Difference between prediction and evaluation?
# Prediction means generating outputs for given input data.
# Evaluation means comparing predictions with actual answers to measure model performance/error.