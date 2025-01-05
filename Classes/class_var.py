# class variables...shared amoug all instances of class
# defined outside of the constractor
#Allows your to share all data amoung all objects created from that class...

class Student:
  
  class_year = 2024
  num_students = 0

  def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students += 1
student1 = Student("vijay",62)
student2 = Student("Koushik",24)
student3 = Student("Latha",50)
student4 = Student("ramana",70)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")

print(student1.name, student1.age)
print(student2.name)
print(student3.name)
print(student4.name)