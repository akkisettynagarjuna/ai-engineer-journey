import pandas as pd

#Load dataSet
df = pd.read_csv("employees_realistic.csv")
print(df)

#dataset inspection
print(df.head()) #head() shows first 5 rows

#dataset information
print(df.info())

#Statistical Summary
print(df.describe())

#Missing Value Analysis
print(df.isnull().sum())

#Fill Missing Values Strategically
df["age"] = df["age"].fillna(df["age"].mean())
df["salary"] = df["salary"].fillna(df["salary"].mean())
df["experience"] = df["experience"].fillna(0)
print(df)

#Feature Engineering Introduction - Creating new useful information from exisitng data called Feature engineering
df["salary_per_experience"] = df["salary"] / (df["experience"] + 1)
print(df)

#Department Analytics
per_dept_avg_sal = df.groupby(by="department")["salary"].mean()
print(per_dept_avg_sal)

#High Salary Employees
high_salary_df = df[df["salary"] > 60000]
print(high_salary_df)

#Sorting Final Dataset
print(df.sort_values(by="salary",ascending=False))

#MINI EXERCISE
# Find employees with experience > 5
# Find average age department-wise
# Find highest salary employee
# Sort employees by experience descending

print(df[df["experience"] > 5])
print(df.groupby(by="department")["age"].mean())
print(df[df["salary"]>50000])
print(df.sort_values(by="experience",ascending=False))

#Bonus Challenge
#Create column called senior_employee , logic : exp > 5 True else False
df["senior_employee"] = df["experience"] > 5
print(df)