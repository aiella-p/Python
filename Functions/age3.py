from datetime import *

name = input("Please enter your Name: ")
age = int(input("Please enter your Age: "))

y = date.today()
x = y.year - age
z = x + 100

print(f"Hello {name}. You will turn 100 years old in the year {z}.")