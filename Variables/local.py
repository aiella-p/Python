# https://www.youtube.com/watch?v=QVdf0LgmICw 
# Variable Scopes in python 
# LEGB - Local, Enclosing, Global and Built-in a common abbrevation in python as LEGB
# Local - vriables defined within the function
# Enclosing - Are variables defined in local scope of enclosing functions
# Globals are - defined at top level of modules explicitly declared global using global keywords
# Buiilt-ins - Are just pre assigned in python

# Note - Python first checks variables in local scope and then enclosing scope , then Global 
# and lastly Built-in scope 

# x = 'global x' # we are defining global string variable
# def test():
#     y = 'local y' # local variable
#     print(y)

# test()    

# Below code checks weather first local variable any avaiable ?? If not, it checks from global if so,
#  it prints that global variable... 
# x = 'global x' # we are defining global string variable
# def test():
#     y = 'local y' # local variable
#     #print(y)
#     print(x)
# test()    


# x = 'global x' # we are defining global string variable
# def test():
#     y = 'local y' # local variable
#     #print(y)
#     print(x) # it will pick from global variable

# test()    
# print(x) # it gets the x variable from global , bcoz this print picks from global bcoz it is outside function

# x = 'global x' # we are defining global string variable
# def test():
#     global x # With this global keyword within function make global variable (x = 'global x') 
#     # as local variable(x = 'local x')
#     x = 'local x' 
#     print(x)

# test()    
# print(x) # This print also printed as 'local x' variable, bcoz of global keyword....

#x = 'global x' # we are defining global string variable
def test():
    global x # With this global keyword within function make global variable (x = 'global x') 
    # as local variable(x = 'local x')
    x = 'local x' 
    print(x)

test()    
print(x) # This print also printed as 'local x' variable, bcoz of global keyword....

#BUILT-IN SCOPE

