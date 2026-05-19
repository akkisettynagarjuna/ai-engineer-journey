import pandas as pd
import matplotlib.pyplot as plt #matplotlib is the most foundational plotting library in python

#create simple line chat
x = [1,2,3,4]
y = [10,20,15,30]
plt.plot(x,y)
plt.show()

#Add Labels and Title
plt.plot(x,y)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Simple Line Chart")
plt.show()
#Question :- why two times plt.plot(x,y) required? As per my guess, plt.plot post that if we use show to see it then the later amendmend on that constructed line grap stiops, so newly we need to con truct it again, and perform all amendmends and then use show to see, is my understanding is correct? 
# plt.plot(x,y) is needed again because after plt.show(), the current plot may get finalized/reset, so later modifications may not apply properly to the previous graph.

# Bar Chat - Bar chats compares categories
departments = ["IT","HR","Finance"]
employees = [50,20,30]
plt.bar(departments,employees)
plt.title("Employees Per Department")
plt.show()

# Histogram
salaries = [40000,50000,60000,60000,70000,80000]
plt.hist(salaries)
plt.title("Salary Distribution")
plt.show() #Histogram shows distribution of numerical values.

# Visualization Using DataFrame
df = pd.read_csv("employees_realistic.csv")
df["salary"] = df["salary"].fillna(df["salary"].mean())
print(df["salary"].sort_values())
plt.hist(df["salary"]) #Histogram
plt.title("Employee Salary Distribution")
plt.show()

# Scatter Plot
df["experience"] = df["experience"].fillna(0)
print(df.sort_values(by="experience"))
plt.scatter(df["experience"],df["salary"])
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")
plt.show()

# Mini Exercise
# Do yourself:

# Create bar chart for department-wise average salary
# Create histogram for employee age
# Create scatter plot:
# age vs salary

plt.figure(figsize=(8,5)) #Controls chat size

dept_wise_avg_sal = df.groupby("department")["salary"].mean()
print(dept_wise_avg_sal)
plt.bar(dept_wise_avg_sal.index,dept_wise_avg_sal.values)
plt.title("Department Wise Average Salary Distribution")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

df["age"] = df["age"].fillna(df["age"].mean())
plt.hist(df["age"])
plt.title("Employee Age Histogram")
plt.xlabel("Age")
plt.ylabel("Number Of Employee(s)")
plt.show()

plt.scatter(df["age"],df["salary"])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()