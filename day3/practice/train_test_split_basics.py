import pandas as pd

from sklearn.model_selection import train_test_split

data = {
    "experience" : [1,2,3,4,5],
    "salary" : [30000,40000,50000,60000,70000]
}

df = pd.DataFrame(data)

# Features
X = df[["experience"]]

# Label
y = df["salary"]

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size = 0.2, #20% data is for testing and remainning is for trainig
    random_state = 42
)

print("X Train")
print(X_train)

print("\nX Test")
print(X_test)

print("\ny Train")
print(y_train)

print("\ny Test")
print(y_test)