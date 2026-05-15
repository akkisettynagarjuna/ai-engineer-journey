def greet():
    print("Hello Nagarjuna")
# greet()

def greet(name):
    print(f"Hello {name}") # Dymanic function
print("Nagarjuna")
print("Mani")

def add(a, b):
    return a + b
result = add(10, 20)
print(result)

# Exercise 1
def square(num):
    return num * num
print(square(2))

def is_even(num):
    return num % 2 == 0
print(is_even(2))
print(is_even(3))

def find_largest(a, b):
    if a > b:
        return a
    return b
print(find_largest(3,2))
print(find_largest(2,3))

def find_smallest(a, b):
    res = a if a < b else b # return a if a < b else b
    return res
print(find_smallest(2,3))
print(find_smallest(3,2))

