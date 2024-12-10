# Iterative and Transfer Keywords: for, while, break, continue, else
# Iterative keywords allow us to execute a block of code repeatedly.
# We also call it a loop statements.

# while: The while loop repeatedly executes a code block while a particular condition is true.
# for: Using for loop, we can iterate any sequence or iterable variable.
#  The sequence can be string, list, dictionary, set, or tuple.



print('for loop to display first 5 numbers')
for i in range(5):
    print(i, end=' ')

print('while loop to display first 5 numbers')
n = 0
while n < 5:
    print(n, end=' ')
    n = n + 1