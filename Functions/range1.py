# for i in range(1, 11):
#     print(i, end=' ')

# Generate numbers between 0 to 6
# for i in range(6):
#     print(i)

# x = range(0,10)[0]
# print(x)

# Print first 10 numbers

# stop = 10
# for i in range(10):
#     print(i, end=' ')

# Output 0 1 2 3 4 5 6 7 8 9

# Numbers from 10 to 15
# start = 10
# stop = 16
# for i in range(10, 16):
#     print(i, end=' ')

# Output 10 11 12 13 14 15

# start = 9
# stop = 100
# step = 3 (increment)
# for i in range(9, 100, 3):
#     print(i, end=' ')

    
# import numpy as np

# # range for floats with np.arange()
# for i in np.arange(0, 4.5, 0.5):
#     print(i, end=', ')
# # Output 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0,

# # Example 2
# for i in np.arange(5.5, 15.5, 2.5):
#     print(i, end=' ')
# # Output 5.5, 8.0, 10.5, 13.0,

# for i in range(1.5, 5.5, 0.5):
#     print("%g" % i, end=", ")
# print('\n')

# for i in range(1, 10, 2):
#     print("Current value of i is:", i)

# for num in range(6):
#     for i in range(num):
#         print(num, end=" ")
#     print()  # new line after each row to show pattern correctly

# # function
# def course_func(name, course_name):
#     print("Hello", name, "Welcome to PYnative")
#     print("Your course name is", course_name)

# # call function
# course_func('vijay', 'Python')

# function
def calculator(a, b):
    add = a + b
    # return the addition
    return add

# call function
# # take return value in variable
# res = calculator(20, 5)

# print("Addition :", res)
# # Output Addition : 25

# function
def even_odd(n):
    # check number is even or odd
    if n % 2 == 0:
        print('Even number')
    else:
        print('Odd Number')

# calling function by its name
# even_odd(190)
# # Output Odd Number

# import randint function
from random import randint

# # call randint function to get random number
# print(randint(10, 20))
# # Output 14

def any_fun(parameter1):
"""              
   Description of function
                 
   Arguments:   
   parameter1(int):Description of parameter1
                 
   Returns:      
   int value     
"""              
print(any_fun.__doc__)