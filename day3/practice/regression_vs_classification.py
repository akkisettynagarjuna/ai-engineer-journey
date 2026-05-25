# Regression : machine predicts numericals/continuous values.
# Classification : machine predicts categories/classes.

import pandas as pd

# Regression Example

salary_data = {
    "experience" : [1,2,3,4],
    "salary" : [30000,40000,50000,60000]
}

salary_df = pd.DataFrame(salary_data)
print("Regression Dataset")
print(salary_df)

# Classification Example

spam_data = {
    "message_lenght" : [100,20,150,10],
    "is_spam" : ["Yes","No","Yes","No"]
}

spam_df = pd.DataFrame(spam_data)
print("\nClassification Datatset")
print(spam_df)

# THEORY QUESTIONS
# What is regression?
# Regression means machine predicts numericals/continuous values.
# What is classification?
# Classification means machine predicts categories/classes.
# Why salary prediction is regression?
# Because it's numericals/continues values. ex :- 30000,40000,50000
# Why spam detection is classification?
# Because it's categories/classes. ex :- Yes/No
# Difference between regression and classification?
# Regression : machine predicts numericals/continuous values.
# Classification : machine predicts categories/classes.
# What is continuous value?
# Continuous values means numerical values where many possible outputs can exist.
# What is category/class?
# category/class means predefined groups like spam/not spam, yes/no, pass/fail.