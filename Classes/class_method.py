# class method - Allows operations with in calss itself...
#Take (cls) as the first parameter, which represents the class itself...But for Instance method we take
# first parameter as (self)

class Student:
    count = 0
    total_gpa = 0 # this variable will accumulate all of the gpa and stored as sum 
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1 # whenever we constract the 
#student object , we will access class Student take count variable increment by 1
        Student.total_gpa += gpa
    #INSTANCE METHOD
    def get_info(self): # Instance method has (self) as first parameter, for class method as (cls)
        return f"{self.name} {self.gpa}"
    
    #CLASS METHOD 
    # To work with class method , we will declare a class method with @classmethod decorator

    @classmethod
    def get_count(cls):
        return f"Total no of students: {cls.count}"
    
    @classmethod
    def get_average_gpa (cls):
        if cls.count ==0: # we will check here 'cls.count == 0:' that means if no students return 0
            return 0
        else:
            return f"{cls.total_gpa / cls.count:.2f}" # this is the way we calculate avg gpa
    # to call the class method...take name of the class followed by class method


#LETS CREATE ONE MORE CLASS METHOD ....TO CALCULATE TOTAL GPA OF ALL STUDENTS...
# WE NEED A CLASS VARIABLE TO HOLD THAT DATA...total_gpa = 0    

# Lets create few student objects...

student1 = Student("Koushik", 5.0)
student2 = Student("vijay", 3.0)
student3 = Student("Latha", 1.2)

print(Student.get_count())
print(Student.get_average_gpa())
