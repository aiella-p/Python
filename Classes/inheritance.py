# Single level inheritance super class A accessed by sub class B

class A:
    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

a1 = A()        
a1.feature1()
a1.feature2()
print(a1.feature1())
print(a1.feature2())

##############################################

# Multilevel inheritance...where the accessing by grand child(C) by parent class(B) and grand father(A)
# class A: class B(A): and class C: 

# super class A, sub class B, and sub class of that super class

##############################################

# Multiple inheritance
# we got class A: and class B: and class C: C is inheritance both the classes A and B
