# if (9 < 0) and (0 < -9):
#  print("hello") 
# elif (9 > 0) or False: 
#  print("good")
# else: 
#  print("bad")
#https://python.plainenglish.io/understanding-the-and-or-operators-in-python-6ac985f9b417
print(bool("")) # Flase

# As we can see, the string contains a space between the quotes.
#  It is important to note that spacein Python is a character, and therefore, the program sees it as a non-empty value, which evaluates to True.
print(bool(" ")) # True

# When it comes to data structures such as lists, sets, tuples, and dictionaries,
# an empty data structure is equivalent to False in Boolean, 
#while any non-empty data structure has a Boolean value of True.

print(bool([]))
print(bool({}))
print(bool(()))