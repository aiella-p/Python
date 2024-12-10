from datetime import datetime

name = input("Enter your name:")
age = int(input("Enter your age:"))
current_year = datetime.now().year
year = str(current_year + (100-age))
print("Hello " + name + ". i find out you become 100 years old in" + " " + year + ".")