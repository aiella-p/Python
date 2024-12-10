#The Python del statement is used to delete objects/variables.

#The target_list contains the variable to delete separated by a comma. 
# Once the variable is deleted, we can’t access it.

x = 10
y = 30
print(x, y)

# delete x and y
del x, y

# try to access it
print(x, y)