import pandas as pd

data = {
    "experience" : [2,5,8],
    "age" : [23,28,35],
    "education" : ["B.Tech","M.Tech","PhD"],
    "salary" : [40000,80000,120000],
    # Practical
    "city" : ["Bangalore", "Hyderabad", "Pune"],
    "favorite_color" : ["Green","Yellow","Orange"]
}

df = pd.DataFrame(data)

print(df)

print("\nFeatures:")
print(df[["experience","age","education","city"]])

print("\nLabel:")
print(df["salary"])

# Theory Questions
# What is feature importance?
# Feature Importance tells us how much each feature contributes to the model's prediction.
# Do all features contribute equally to predictions?
# It depends , based on the business data we can say that. My peersonal opinion the data can be any type I believe atleast one irrelavent data will be there for prediction henece I beilevely not all features contribute equally to predictions. Irrelevant means for the industry or business it's relevant but predictions it's irrelevant.
# Why is choosing the right features important?
# Becuase chossing the right features important which makes our model predications perfectly/most accurately.
# Can irrelevant features reduce model performance?
# Irrelevant features can reduce model performance because they may introduce noise and confuse the learning process.

# Practical
# Do you think city might influence salary?
# Why?
# It Depends.
# Do you think favorite_color influence salary prediction?
# Why or why not?
# No, it will not influence salary prediction
# Bs it's a persons personal thing not a skill where it helps in his/her job to help.