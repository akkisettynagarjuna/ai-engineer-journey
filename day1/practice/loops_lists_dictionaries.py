# Lists
numbers = [10,20,30,40,50]
print(type(numbers)) # why? Because I want to check the data type of the variable 'numbers' to confirm that it is a list.
print(numbers)
print(numbers[0])
print(numbers[1])
numbers.append(60)
print(numbers)
numbers.remove(20)
print(numbers)

# Loops
for num in numbers:
    print(f"{type(num)}: {num}")

total = 0

for num in numbers:
    total = total + num

print(f"Total : {total}")

# Dictionaries
employee = {
    "name" : "Sasank",
    "age" : 24,
    "salary" : 50000.00
}
print(employee)
print(employee["name"])
print(employee["age"])

employee["name"] = "Manish" # we can update the value of a key in a dictionary by using the key and assigning a new value to it.

print(employee)
print(employee["name"])

employee["city"] = "Bangalore" # we can also add new key-value pairs to a dictionary by using the key and assigning a value to it.

print(employee)
print(employee["city"])

# Loop through dictionary
for key,value in employee.items(): # items() method gives key-pairs in a dictionary as tuples, which we can unpack into key and value variables in the loop.
    print(key,value)

print(type(employee))    
print(type(employee.items()))

# Mini Exercise
# Do this YOURSELF.

# Create:

# students = []

# Take 3 student names using input.

# Add them into list.

# Finally print all students using loop.

students = [] # In memory at this point it's an empty list.

count = 1

while count < 4: 
    students.append(input(f"Enter Student {count} name : "))
    count = count + 1

print(students) # In memory at this point it contains list of three elements type string

# Feedback
# Cleaner version : while count <=3:
# Even better : for count in range(1, 4):

# BONUS CHALLENGE (TRY)

# Create dictionary:

# student = {
#     "name": "ABC",
#     "marks": 90
# }

# Print:

# ABC scored 90 marks

# using:

# f-string

student = {
    "name" : "Mani",
    "marks" : 100
} # In memory dist will store.

print(f"{student["name"]} scored {student["marks"]} marks") # This will not work with older python versions <3.12
# Best Industry practice is to print(f"{student['name']} scored {student['marks']} marks")
print(f"{student['name']} scored {student['marks']} marks")