#In Python, while loop inside a while loop is known as nested loop.

#In the nested while loop, the number of iterations will be equal 
# to the number of iterations in the outer loop multiplied by the iterations 
# in the inner loop. 
# In each iteration of the outer loop inner loop execute all its iteration.

i = 1
# outer while loop
# 4 rows in pattern
while i < 5:
    j = 0
    # nested while loop
    while j < i:
        print('*', end=' ')
        j = j + 1
    # end of nested while loop
    # new line after each row
    print('')
    i = i + 1
