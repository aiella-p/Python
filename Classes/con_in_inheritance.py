# Constructors in Inheritance
# sub class can access all the features of Super class , but super class cannot access 
# any feature of sub classes...
# As below code when we create object of sub class it will call init of sub class first
# If you have call 'super' then it will first call init of Super class then call 
# init of Sub class...  
class A:

    def __init__(self):
        super().__init__()
        print("In A init")
        
    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

class B(A):
    def __init__(self):
        super().__init__() # we are calling super class and it prints first (In A init)
        print("In B init")

    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")        

a1 = B()