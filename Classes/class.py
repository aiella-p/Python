# class Person:
#     def __init__(self, name, sex, profession):
#         # data members (instance variables)
#         self.name = name
#         self.sex = sex
#         self.profession = profession

#     # Behavior (instance methods)
#     def show(self):
#         print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

#     # Behavior (instance methods)
#     def work(self):
#         print(self.name, 'working as a', self.profession)

class Student:

    # constructor
    # initialize instance variable
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name
        print('All variables initialized')

    # instance Method
    def show(self):
        print('Hello, my name is', self.name)


# create object using constructor
s1 = Student('Emma')
s1.show()