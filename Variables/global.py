# python-global-variable.py
a = 100
#print('Value of a is ->',a)
def function_local():
        global a # with this global keyword new value for 'a' variable is 100
        print('a is -> ',a)
        a = 50 # local varible to function
        print('After new value within the function a is -> ',a)

function_local()
print('Value of a is ->',a) # THis print statement prints the local variable a=50, bcoz this a=50 
# is local to the fuction
