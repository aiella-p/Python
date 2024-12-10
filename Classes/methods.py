# Instance methed, class methods and static methods...
class student:
    school = "Telusuko" # class variable

    def __init__(self,m1,m2,m3):
        self.m1 = m1 # instance variable self.m1
        self.m2 = m2
        self.m3 = m3

# calculate average marks of students....same above code with ...below code
    def avg(self): # Instance method...
     return(self.m1 + self.m2 + self.m3)/3 # this is instance method...

s1 = student(35,33,44) # creating object by name s1
s2 = student(32,37,48) # creating object by name s2

print(s1.m3)
print(s2.m1)
print(s1.avg())
print(s2.avg())

################################

# Instance has two method types 
#Access Methods - when fetching only values...are AM, it will only get the values as below..
# and it does not change the values..
def get_m1(self):
   return self.m1
# Mutator Methods are setters they change the values... If we want to modify the values we use Mutators...

def set_m1(self,value):
   return self.m1

#################################

# class methods...
# if we are working with instance variables we use 'self' keyword
# if your working with class variables we have to use 'cls' keyword as below..

class student:
    school = "Telusuko" # class variable

    def __init__(self,m1,m2,m3):
        self.m1 = m1 # instance variable self.m1
        self.m2 = m2
        self.m3 = m3

# calculate average marks of students....same above code with ...below code
    def avg(self): # Instance method...
     return(self.m1 + self.m2 + self.m3)/3 # this is instance method...

    @classmethod # we have to use @classmethod decorators
    def getSchool(cls):
     return cls.school
    
    # @staticmethod
    def info():
       print("this is student class in abc module")

s1 = student(35,33,44) # creating object by name s1
s2 = student(32,37,48) # creating object by name s2

print(s1.m3)
print(s2.m1)
print(s1.avg()) 
print(s2.avg())

print(student.getSchool())
student.info()