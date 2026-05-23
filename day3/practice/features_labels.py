import pandas as pd

data = {
    "experience" : [1,2,3,4],
    "age" : [22,25,30,35],
    "salary" : [30000,40000,50000,60000]
}

df = pd.DataFrame(data)

print(df)

# Features
x = df[["experience","age"]]

# Label
y = df["salary"]

print("\nFeatures:")
print(x)

print("\nLabel:")
print(y)

# THEORY QUESTIONS
# What are features?
# Features are the input variables given to the ML model for predictions.
# What is label?
# Label is the correct output/target value that the ML model tries to predict.
# Why salary is label?
# Salary is label because it is the target output we want the ML model to predict.
# Why experience is feature?
# Because it's used for prediction.
# Can features have multiple columns?
# Yes, we can have.
# Can irrelevant features affect ML models?
# Yes, irrelevant features can negatively affect ML models by introducing noise and reducing prediction accuracy.