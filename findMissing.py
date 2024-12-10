
#FINDING MISSING NUMBERS FROM LIST


# mylist = [1,2,3,4,6]

# def findMissing(list, n):
#    sum1 = 5*6/2   # n * (n + 1)/2 = 5 * (5 + 1)/2 = 15
#    sum2 = sum(list)
#    print(sum1-sum2)
# findMissing(mylist, 5)

# we need to find missing values from below list....(ex: 3,8)
# a = [1,2,4,5,6,7,9,10]
# b = [] # create an empty list
# for i in range(a[0],a[-1]): # Here we have to take in the range function a[0] minimum value
#                              # and a[-1] maximum value in the index
#     if i not in a: 
#         b.append(i)    # we are requesting the values 
#         #from a list which were missing from the range function(that is 3,8)
# print(b)

#2nd Method for above issue

a = [1,2,4,5,6,7,9,10]
res = [] # create an empty list
for i,j in zip(a,a[1:]): # Here we have to take in the range function a[0] minimum value
    if j-i>1:
        for k in range(i+1,j):
            res.append(k)                         # and a[-1] maximum value in the index
     
print(res)


