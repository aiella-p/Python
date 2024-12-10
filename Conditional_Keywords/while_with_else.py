# In Python, we can use the else block in the while loop, 
# which will be executed when the loop terminates normally. 
# Defining the else block with a while loop is optional.
# The else block will not execute in the following conditions:
# while loop terminates abruptly
# The break statement is used to break the loop

i = 1
while i <= 5:
    print(i)
    i = i + 1
else:
    print("Done. while loop executed normally")