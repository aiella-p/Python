# Python variables SCOPE
# lOCAL VARIABLES
#GLOBAL VARIABLES
#NONLOCAL VARIABLES

#LOCAL VARIABLES

# def showEmployeeDetails():
#     age = 45
#     print(age)

#showEmployeeDetails()
#print(age)

#GLOBAL VARIABLES
age = 45
def showEmployeeDetails():
    print(age) # Inside the function is possible to access the global variable
def showEmployeeDetails1(): 
    print(age) # Inside the function is possible to access the global variable

showEmployeeDetails()    
showEmployeeDetails1()
print(age) # outside the function is also possible to access the global variable

#NONLOCAL VARIABLES

# In python non local variables are used in Nested functions, whose local scope is not defined
# It means the variable either local or global scope

def showEmployeeSalary():
    salary = 2000
    def getSalary():
        nonlocal salary
        salary = 3000
        print("Salary Inside: ",salary)
    getSalary()
    print("Salary Outside: ", salary)    
showEmployeeSalary()        
