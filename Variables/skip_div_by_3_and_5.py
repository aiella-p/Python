# We need to print 1 to 100 expect the numbers which are divisible by 3 and 5 !!

# for i in range(1,11):
#     if i%3 == 0 or i%5 ==0: # if i divided by 3 equal to 0 and i divided by 5 equal to 0, it will continue the range function
#         continue
#     print(i)

for i in range(1,11):
    if i%3 == 0 and i%5 ==0: # if i divided by 3 equal to 0 and i divided by 5 equal to 0, it will continue the range function
        continue
    print(i)