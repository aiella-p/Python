#We can also use for loop inside a while loop as a nested loop. 
# Let’s see the same example using for loop inside the while loop.


i = 1
# outer while loop
while i < 5:
    # nested for loop
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')
    i = i + 1