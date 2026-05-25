import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = {
    "experience" : [1,2,3,4,5],
    "salary" : [30000,40000,50000,60000,70000]
}
df = pd.DataFrame(data)
print("exp_sal_dataset")
print(df)
# Features
X = df[["experience"]]
# Label
y = df["salary"]
# train_test_split data
X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
# Features for model training
print("Features for model training")
print(X_train)
# Label for model training
print("\nLabel for model training")
print(y_train)

# Features for model testing
print("\nFeatures for model testing")
print(X_test)
# Label for model evaluation
print("Label for model evaluation")
print(y_test)

# This line creates empty ML model, at this moment no learning happened yet.
model = LinearRegression()

# This line performs actual machine learning. Machine studies X_train, y_train and tries to learn relationship/pattren.
model.fit(X_train,y_train)

# Prediction
prediction = model.predict([[6],[7]])
print(prediction)
# model.predict([[6],[7]]) this is plain array no column names exist. So sklearn says : "Hey, during training feature names existed, but during prediction feature names missing." Only warning. Prediction still works.

# Professional way
# Better prediction:
prediction_data = pd.DataFrame({
    "experience" : [6,10]
})
prediction = model.predict(prediction_data)
print(prediction)# Now warning disappears because feature names consistent.

# Very important ML Engineering lesson
# In real ML systems : training input structure and prediction input structure should remain consistent.
# Very important engineering principle.

# THEORY QUESTIONS
# What is model in ML?
# Model in ML is to learn hidden pattrens/relationships from data for future predicion.
# What does fit() do?
# fit() trains the model by learning pattrens from training data.
# What does predict() do?
# predict() uses learned patterns to predict outputs for new input data.
# Did model learn before fit()?
# No
# Why prediction possible for unseen input?
# Bs model uses the pattrens to find the output for the unseen input , it will not just memorizes the trainned data examples. In shory it's a Good ML model , not the overfit model.
# What is Linear Regression intuition?
# Linear Regression tries to learn stratight-line relationship berween variables. ex:- experience increases -> salary increases.