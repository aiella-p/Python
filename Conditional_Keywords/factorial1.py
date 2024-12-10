# Write a Python program to use for loop to find the factorial of a given number.

# The factorial (symbol: !) means multiplying all numbers from the chosen number down to 1.

# For example, a factorial of 5! is 5 × 4 × 3 × 2 × 1 = 120


# Set variable factorial = 1 to store the factorial of a given number
# Iterate numbers starting from 1 to the given number n using for loop and range() function. (here, the loop will run five times because n is 5)
# In each iteration, multiply the factorial by the current number and assign it again to a factorial variable (factorial = factorial *i)
# After the loop completes, print factorial

num = 5
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # run loop 5 times
    for i in range(1, num + 1):
        # multiply factorial by current number
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)


