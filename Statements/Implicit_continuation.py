# Implicit continuation:

# We can use parentheses () to write a multi-line statement. 
# We can add a line continuation statement inside it. 
# Whatever we add inside a parentheses () will treat as a single statement even 
# it is placed on multiple lines.

# Example:

addition = (10 + 20 +
            30 + 40 +
            50 + 60 + 70)
print(addition)
# Output: 280

# As you see, we have removed the the line continuation character (\)
#  if we are using the parentheses ().

# We can use square brackets [] to create a list. Then, if required, 
# we can place each list item on a single line for better readability.
# Same as square brackets, we can use the curly { } to create a dictionary with every key-value pair
#  on a new line for better readability.

# Example:

# list of strings
names = ['Emma',
         'Kelly',
         'Jessa']
print(names)

# dictionary name as a key and mark as a value
# string:int
students = {'Emma': 70,
            'Kelly': 65,
            'Jessa': 75}
print(students)