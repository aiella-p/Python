# We need to print 1 to 100 expect the numbers which are divisible by 3

for i in range(1,11):
    if i%3 == 0: # if i divided by 3 equal to 0, it will continue the range function
        continue
    print(i)