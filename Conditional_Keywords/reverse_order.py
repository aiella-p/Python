# Approach 1: Use the built-in function reversed() to reverse the list

# Approach 2: Use for loop and the len() function

# Get the size of a list using the len(list1) function
# Use for loop and reverse range() to iterate index numbers in reverse order,
#  starting from length-1 to 0. In each iteration, i will be reduced by 1
# In each iteration, print list items using list1[i].
#  i is the current value of the index


list1 = [10, 20, 30, 40, 50]
# reverse list
new_list = reversed(list1)
# iterate reversed list
for item in new_list:
    print(item)
