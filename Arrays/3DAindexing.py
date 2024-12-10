#3 Dimensional layer with two layer Example... 
# # Three Dimensional Array - Is nothing but combining of two two dimensional arrays are called Three Dimensional array
# # Array of Shape (2,2,3) - First 2 represents number of 2 Dimensional arrays.....[(2,3) are represents number
# # of rows and number of columns respectively]

# # First 2D array...
# import numpy as np
# arr1 =  np.array([ [1,2,3],[4,5,6] ])
# arr2 =  np.array([ [7,8,9],[10,11,12] ])
# print(arr1)
# print(arr1.shape)

# # Second 2D array...
# print(arr2)
# print(arr2.shape)

# # Three Dimensional array ....(combining above two two dimensional array)

# arr3 = np.array([ [ [1,2,3],[4,5,6] ], [ [7,8,9],[10,11,12] ] ])
# print(arr3)
# print(arr3.shape)

# 3 Dimenstional array with 3 layers....

# Three Dimensional Array - Is nothing but combining of three two dimensional arrays are called Three Dimensional array
# Array of Shape (3,2,3) - First 3 represents number of 2 Dimensional arrays.....[(2,3) are represents number
# of rows and number of columns respectively]

# First 2D array...
import numpy as np
arr1 =  np.array([ [1,2,3],[4,5,6] ])
print(arr1)
print(arr1.shape)

# Second 2D array...
arr2 =  np.array([ [7,8,9],[10,11,12] ])
print(arr2)
print(arr2.shape)

# Third 2D array...
arr3 =  np.array([ [13,14,15],[16,17,18] ])
print(arr3)
print(arr3.shape)

# Three Dimensional array ....(combining above three two dimensional arrays)

arr3 = np.array([ [[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]], [[13,14,15],[16,17,18]] ] )
print(arr3)
print(arr3.shape)

