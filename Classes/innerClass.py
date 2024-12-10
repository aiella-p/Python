class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
         print("computer details: ", self.brand,self.cpu,self.ram)    

s1 = student('navin',10)
s2 = student('vijay',20)

print(s1.name,s2.rollno) 
s1.show()       
s2.show()