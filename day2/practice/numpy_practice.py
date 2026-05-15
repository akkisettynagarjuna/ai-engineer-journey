import numpy as np

#step 1 : Create NumPy Array
numbers = np.array([1,2,3,4,5]) # This is not python list, this is Numpy ndarray special optimized structure.
print(numbers)
print(type(numbers))

#step 2 : Array Operations
print(numbers+10) # Very IMP : Numpy performs vectorized operations(operation applied to all elements efficiently)

#step 3 : Compare with python list
# n = [1,2,3,4,5]
# print(n+10) # Error : TypeError: can only concatenate list (not "int") to list # so this will acheiveable print(n+[6]) = [1, 2, 3, 4, 5, 6]

#step 4 : Array Multiplication
print(numbers*2)

#step 5 : Mean Calculation
print(numbers)
print(np.mean(numbers)) # average # VERY important in ML/statistics.

#step 6 : Shape
print(numbers)
print(numbers.shape) # dimensions of array # VERY important later for ML.

#step 7 : 2D Arrays
nums = np.array(
    [
        [1,2,3],
        [4,5,6]
    ]
)
print(nums)
print(nums.shape) # rows x cols

#MINI EXERCISE
arr = np.array([5,10,15,20])
print(arr*3)
print(arr+5)
print(np.mean(arr))
print(np.shape(arr))
print(arr.shape)

#Bonous Question
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))

#Final Practice
arr = np.array([5, 10, 15, 20])

print(arr.shape)

row_matrix = np.array([[5, 10, 15, 20]])
print(row_matrix.shape)

column_matrix = np.array([[5], [10], [15], [20]])
print(column_matrix.shape)

print(arr.mean())
print(np.mean(arr))