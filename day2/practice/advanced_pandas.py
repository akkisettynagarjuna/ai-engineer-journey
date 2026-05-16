import pandas as pd
import numpy as np

#step 1 : Create Dataset with Missing Values
data = {
    "name" : ["Nagarjuna", np.nan, None, "Rayudu"],
    "age" : [24,np.nan,59,29],
    "salary" : [50000,60000,None,70000]
} # return type is dict[str,list] 
# We introduced np.nan and None these represents the missing values. Very common in real datasets.
# diff between np.nan and None ? when and what we should be chossing?
# Generally in db / java we tell that if it is empty string then it is a missing value, how it differ here? and corrcet me the thing I'm saying for java and db is wrong? Also tell in others like db , java how there it will act? Or should I not compare at all with db / java bs there are table, the one which we are working are dataset.
df = pd.DataFrame(data)
print(df)

#step 2 : Detect Missing Values
detect_missing_values = df.isnull()
print(detect_missing_values) # Creates True/False dataframe.

#step 3 : count missing values
count_missing_values_for_each_Section = df.isnull().sum() # adds True 1 , False 0 so result becomes number of missing values # return typr series[Any] # Very important preprocessing technique.
print(count_missing_values_for_each_Section)

#step 4 : Drop missing values
clean_df =  df.dropna() #removes rows that contains missing values. #very commom preprocessing step.
print(clean_df)
#IMP : Sometime dropping rows is dangerous because valuable data may get lost so engineers decide carefully.

#step 5 : Fillinng missing values.
#Instead of removing rows :
filled_df = df.fillna(0) # Missing values replcaed with 0 is called imputation. # Very important ML preprocessing concept.
print(df)
print(filled_df)

#step 6 : Fill Specific Column
df["age"] = df["age"].fillna(df["age"].mean()) #This is real world preprocessing. Instead of randon values we use statistical value like mean, median #Very common in ML
print(df)

#step 7 : Sorting - rows sorted based on column
print(df.sort_values(by="age")) # no missing values present.
print(df.sort_values(by="salary")) # missing value present. # missing salary row always kept at bottom.

print(df.sort_values(by="age",ascending=False)) #by default the ascending value will be True #so decsinding will apply here.
print(df.sort_values(by="salary",ascending=False))#by default the asceding value will be True #so desceinding will apply here. #same story the missing value row goes at bottom.

#step 8 : Aggregation - It means summarizing the data #very important in analytics
print(df["salary"].mean())
print(df["salary"].max())
print(df["salary"].min())

#step9 : Group By #vey IMP
data = {
    "department" : ["IT","IT","HR","HR"],
    "salary" : [50000,60000,30000,40000]
}
df = pd.DataFrame(data)
print(df)
groupby_by_dept = df.groupby("department")
print(pd.DataFrame(groupby_by_dept))
mean_salary_of_each_Dept = groupby_by_dept["salary"].mean()
print(mean_salary_of_each_Dept)
#Why GorpBy is HUGE
#Used heavily in :
# analytics
# dashboards
# business intelligence
# feature engineering
# Very IMP

#MINI Exercise
data = {
   "name" : ["A","B","C"],
   "marks" : [90,np.nan,80]
}
df = pd.DataFrame(data)
print(df)
# Tasks:

# detect nulls
# count nulls
# fill NaN with mean marks
# sort marks descending

detect_nulls = df.isnull()
print(detect_nulls) #creates True/False DataFrame
count_nulls = detect_nulls.sum() #step 1 : detect step 2 : sum => count achieved.
print(count_nulls)
#fill_nan_with_mean_marks
df["marks"] = df["marks"].fillna(df["marks"].mean())
print(df)
sort_marks_desc_df = df.sort_values(by="marks",ascending=False)
print(sort_marks_desc_df)

#BONUS CHALLENGE

# Create department-wise employee salaries and:

# calculate max salary per department
# calculate average salary per department

#Basic step : data -> dataframe(so that clean format structure data will be formed and we can perform n number of operations on that data like Excel)
data = {
    "dept" : ["IT","IT","IT","HR","HR","HR"],
    "sal" : [100000,90000,80000,50000,40000,30000]
}
df = pd.DataFrame(data)
print(df)

#performing group by so that per dept now we can apply operations.
groupby_by_dept = df.groupby("dept")

#max salary per dept
print(groupby_by_dept["sal"].max())

#average salary per dept
print(groupby_by_dept["sal"].mean())
