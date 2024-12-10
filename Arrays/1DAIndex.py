import numpy as np
arr1 = np.array([1,2,3,4,5,6])
print(arr1)
print(arr1[1]) # 2
print(arr1[4]) # 5
print(arr1[5]) # 6
print(arr1[3]) # 4

# We can also perform maths operations on ND arrays 
# Mul
print(arr1[2] * arr1[3])

# Div
print(arr1[2] / arr1[3])

# Floor Div
print(arr1[2] // arr1[3])

# Subtraction
print(arr1[2] - arr1[3])