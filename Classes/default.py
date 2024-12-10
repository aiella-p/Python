#default constractor
#As you can see in the example, we do not have a constructor, 
#but we can still create an object for the class because Python added the default constructor
# during a program compilation.

class Employee:

    def display(self):
        print('Inside Display')

emp = Employee()
emp.display()

# Non-Parametrized Constructor
# A constructor without any arguments is called a non-parameterized constructor. 
# This type of constructor is used to initialize each object with default values.

#This constructor doesn’t accept the arguments during object creation. Instead, 
# it initializes every object with the same set of values.

class Company:

    # no-argument constructor
    def __init__(self):
        self.name = "PYnative"
        self.address = "ABC Street"

    # a method for printing data members
    def show(self):
        print('Name:', self.name, 'Address:', self.address)

# creating object of the class
cmp = Company()

# calling the instance method using the object
cmp.show()

# Parameterized Constructor
# A constructor with defined parameters or arguments is called a parameterized constructor.
# We can pass different values to each object at the time of creation using a parameterized constructor.

#The first parameter to constructor is self that is a reference to the being constructed, and the rest of the arguments are provided by the programmer. 
# A parameterized constructor can have any number of arguments.

# class Employee:
#     # parameterized constructor
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     # display object
#     def show(self):
#         print(self.name, self.age, self.salary)

# # creating object of the Employee class
# emma = Employee('Emma', 23, 7500)
# emma.show()

# kelly = Employee('Kelly', 25, 8500)
# kelly.show()

# Constructor With Default Values
# Python allows us to define a constructor with default values.
# The default value will be used if we do not pass arguments to the constructor at the time of
# object creation.
# The following example shows how to use the default values with the constructor.

class Student:
    # constructor with default values age and classroom
    def __init__(self, name, age=12, classroom=7):
        self.name = name
        self.age = age
        self.classroom = classroom

    # display Student
    def show(self):
        print(self.name, self.age, self.classroom)

# creating object of the Student class
emma = Student('Emma')
emma.show()

kelly = Student('Kelly', 13)
kelly.show()

