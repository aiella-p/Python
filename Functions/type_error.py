# def display_person(*args):
#     for i in args:
#         print(i)

# display_person(name="Emma", age="25")


#OR

# def display_person(*args):
#     for i in args:
#         print(i)

# display_person("Emma", "25")

# def displayPerson(**kwargs):
#     print(kwargs)
# displayPerson(name="Emma", age=25)

#Use *args to get the variable number of positional arguments.

# def print_numbers(*args):
#     print(args)
# print_numbers(5, 23, 45, 78)


# #To accept Variable Length of Keyword Arguments, i.e., To create functions that take n number of Keyword arguments we use **kwargs (prefix a parameter name with a double asterisk ** ).
# def display(**kwargs):
#     for i in kwargs:
#         print(i)

# display(emp="Kelly", salary=9000)

def display(**kwargs):
#    for i in kwargs:
        print(kwargs)

display(emp="Kelly", salary=9000)


