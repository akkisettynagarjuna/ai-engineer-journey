name = "Mani"
age = 59
salary = 184000.50
is_engineer = False # NameError: name 'false' is not defined. Did you mean: 'False'?

print(name)
print(age)
print(salary)
print(is_engineer)

name = input("Enter your name : ") # input always returns a string
print("Hello " + name)

# Type conversion
# age = input("Enter your age : ")
# print("Your age is " + (20 + age)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# To resolve this error, I need to type conversion
age = int(input("Enter your age : ")) # String to int type conversion
print("Your age is " + str(20 + age)) # int to String type conversion

# SUPER IMPORTANT Type Conversion functions
# int() - converts a value to an integer
# float() - converts a value to a floating-point number
# str() - converts a value to a string
# bool() - converts a value to a boolean

# Mini Exercise
# Create program:

# Ask:

# name
# age
# city

# Output:

# Hello Nagarjuna
# You are 25 years old
# You live in Bangalore

name = input("Enter your name : ") # why? Because I want to get the user's name and store it in a variable called 'name' for later use in the program.
age = int(input("Enter your age : ")) # why? Because I want to get the user's age and store it in a variable called 'age' for later use in the program. I also want to convert the input from a string to an integer so that I can perform arithmetic operations on it if needed.
city = input("Enter your city : ") # why? Because I want to get the user's city and store it in a variable called 'city' for later use in the program.
print("Hello " + name) # why? Because I want to greet the user by their name.
print("You are " + str(age) + " years old") # why? Because I want to inform the user about their age. I also need to convert the age back to a string to concatenate it with the other strings in the print statement.
print("You live in " + city) # why? Because I want to inform the user about their city of residence.

# we can also use f-strings for better readability
print(f"Hello {name}") # f-string allows us to embed expressions inside string literals,
print(f"You are {age} years old") # f-string allows us to embed expressions inside string literals,
print(f"You live in {city}") # f-string allows us to embed expressions inside string literals,