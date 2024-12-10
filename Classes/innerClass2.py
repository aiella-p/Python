# we need to check below code...
class NameOfOuterClass:
  # Constructor method of outer class
  def __init__(self):  
    self.NameOfVariable = 1
    # create Inner class object
    self.NameOfInnerClassObject = self.NameOfInnerClass() 
 
  # create a NameOfInnerClass class
  class NameOfInnerClass:  
     # Constructor method of inner class
    def __init__(self): 
      self.NameOfVariable = 2
# create object of outer class
outer = NameOfOuterClass() 
print(outer)