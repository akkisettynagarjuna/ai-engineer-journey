import pandas as pd

from sklearn.linear_model import LinearRegression

data = {
    "experience" : [1,2,3,4,5,6,7],
    "salary" : [32000,41000,47000,65000,69000,85000,92000]
}

df = pd.DataFrame(data)

# Features
X = df[["experience"]]

# Label
y = df["salary"]

# Model
model = LinearRegression()

# Training
model.fit(X,y)

# Future Prediction
pred_sal_df = pd.DataFrame({
    "experience" : [7]
})
prediction = model.predict(pred_sal_df)
print("Predicted Salary:")
print(prediction) # [93200.] before adding the exp 7 and sal 92000 in dataset , [92642.85714286] after adding the exp 7 and sal 92000 in dataset

# Theory Questions
# Why is this dataset more realistic than previous datasets?
# Real-world data usually contains variations and irregularities. Values do not increase in prefectly equal increments like our earlier datasets.
# Does real-world data always follow perfect patterns?
# No.
# Why can Linear Regression still work even when data is not perfect?
# Linear Regression tries to find the overall trend in data, even when data is imperfect.

# Practical Questions
# Add:
# experience = 7
# salary = 92000

# to dataset and rerun.

# Observe whether prediction changes.
# Yes predicion changed, the model didn't simple meorized the salary provided in the dataset it actually performed the pattren it learned and provided this outcome : 92642.85714286

# Predict salary for:
# experience = 10

# and see output.

pred_sal_df = pd.DataFrame({
    "experience" : [10]
})
prediction = model.predict(pred_sal_df)
print("Predicted Salary:")
print(prediction)