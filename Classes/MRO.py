# Method Resolution Order... 

class A:

    def __init__(self):
        print("In A init")
        
    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

class B:

    def __init__(self):
        print("In B init")

    def feature1(self):
        print("feature 1-B working")

    def feature4(self):
        print("feature 4 working")        

class C(A,B):

    def __init__(self):
        super().__init__() # we are calling super class and it prints first (In A init) 
        # then In C init , bcoz it calls in order from left to right class C(A,B): this is 
        # called Method Resolution Order...
        print("In C init")
     
a1 = C()
a1.feature1()