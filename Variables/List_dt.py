# # The Python List is an ordered collection (also known as a sequence ) of elements. List elements can be accessed, iterated, and removed according to the order they inserted at the creation time.

# # We use the list data type to represent groups of the element as a single entity.  For example: If we want to store all student’s names, we can use list type.

# # The list can contain data of all data types such as  int, float, string
# # Duplicates elements are allowed in the list
# # The list is mutable which means we can modify the value of list elements

# We can create a list using the two ways

# By enclosing elements in the square brackets [].
# Using a list() class.

my_list = ["Jessa", "Kelly", 20, 35.75]
# display list
print(my_list)  # ['Jessa', 'Kelly', 20, 35.75]
print(type(my_list))  # class 'list'

# Accessing first element of list
print(my_list[0])  # 'Jessa'

# slicing list elements
print(my_list[1:5])  # ['Kelly', 20, 35.75]

# modify 2nd element of a list
my_list[1] = "Emma"
print(my_list[1])  # 'Emma'
print(my_list)

# create list using a list class
my_list2 = list(["Jessa", "Kelly", 20, 35.75])
print(my_list2)  # ['Jessa', 'Kelly', 20, 35.75]

