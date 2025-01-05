# An event that interrupts the flow of a program
# (ZeroDivisionError, TypeError, ValueError)
# 1. try 2. except 3. finally

# ZeroDivisionError - 
#1/0

# TypeError -
# a= 1 + "2"
# print(a)

# # ValueError -
# b = int("someName")
#print(b)

try:
 number = int(input("Enter a Number: "))
 print(1 / number)    
      
except ZeroDivisionError:
    print("You can't divide by zero FOOL !!")

except ValueError:
    print("Enter only numbers ..Plz !!")

finally:
   print("Do some cleanup here")    

 
