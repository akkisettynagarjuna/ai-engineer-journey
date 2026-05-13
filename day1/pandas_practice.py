#Step 1 : Import Pandas
import pandas as pd

#Step 2 : Create DataFrame
data = {
    "name" : ["Nagarjuna", "Mani", "Rayudu"],
    "age" : [24, 59, 29],
    "salary" : [100.5, 200.5, 300.5]
}
df = pd.DataFrame(data)
print(df)
print(type(df))

#Step 3 : Access Columns
# Single Column
# return type is Series of Any
print(df["age"]) # row counts will come in display and no header will be there also at the end it prints the column name and type
# return type is DataFrame
print(pd.DataFrame(df["age"]))
# return type is DataFrame
print(df[["age"]])
# Multiple Columns
print(df[["name","age"]]) # No special display like single column , it prints in normal nice tabular form
#step 4 : Filtering Rows
# df["age"] > 24 creates True/False masks.
# pandas keeps only True rows, so df[True/False] => only df[True] , Hence df[df["age"] > 24]
filter_age = df["age"] > 24 #return type is Series[bool]
data_post_age_filter = df[filter_age] # Pandas keeps only True(s) rows... False drops.
print(data_post_age_filter) # print(df[df["age"] > 24])

#step 5 : Add New Column
df["bonus"] = df["salary"] * 2
print(df)

#step 6 : Read CSV File
df = pd.read_csv("employees.csv")
print(df)

#step7 : CSV Filtering

df = df[df["salary"] >= 60000]
print(df)

# Mini Exercise
students_df = pd.read_csv("students.csv") # return type is DataFreame so when we print we can see table fromatterd sturctured data like excel.
print(students_df)
students_80_above_marks = students_df["marks"] > 80 # return type is series of bool
print(students_80_above_marks)
students_80_above_marks_df = students_df[students_80_above_marks] # return type is DataFreame so when we print we can see table fromatterd sturctured data like excel.
print(students_80_above_marks_df)
print(students_df[[True,False,True]]) # return type is DataFreame so when we print we can see table fromatterd sturctured data like excel.