# Python writing files (.txt,.json and csv)

# txt_data = "I like pizza"
# file_path = "output.txt"

# with open(file_path, "w") as file: # note here 'with' is statement and w is write mode , 'x' is also write mode
# # if 'output.txt doesn't exists will creates it !
# # 'a' is for append the file and 'r' is for read file
#   file.write(txt_data)    
#   print(f"txt file '{file_path}'was created")

#   #########################################
#   #
# txt_data = "I like pizza1"
# file_path = "C:/Users/oracl/Desktop/test/output.txt"

# with open(file_path, "w") as file: # note here 'with' is statement and w is write mode , 'x' is also write mode
# # if 'output.txt doesn't exists will creates it !
# # 'a' is for append the file and 'r' is for read file
#   file.write(txt_data)    
#   print(f"txt file '{file_path}'was created")


  #########################################
  # Exception FileExistsError
# txt_data = "I like pizza1"
# file_path = "C:/Users/oracl/Desktop/test/output.txt"

# try:
#  with open(file_path, "x") as file: # note here 'with' is statement and w is write mode , 'x' is also write mode
# # if 'output.txt doesn't exists will creates it !
# # 'a' is for append the file and 'r' is for read file
#   file.write(txt_data)    
#   print(f"txt file '{file_path}'was created")

# except FileExistsError:
#    print("That file already exists")

##################################
# appending that textfile with data in '\n' new line

# txt_data = "I like pizza1"
# file_path = "C:/Users/oracl/Desktop/test/output.txt"

# try:
#  with open(file_path, "a") as file: # note here 'with' is statement and w is write mode , 'x' is also write mode
# # if 'output.txt doesn't exists will creates it !
# # 'a' is for append the file and 'r' is for read file
#   file.write("\n" + txt_data)    
#   print(f"txt file '{file_path}'was created")

# except FileExistsError:
#    print("That file already exists")

# #######################################
# # We can get the list of the employee from list object...
   
# employees = ["Vijay","Ramana","Rakesh","Koushik"]
# file_path = "C:/Users/oracl/Desktop/test/output.txt"

# try:
#  with open(file_path, "w") as file:
#   for employee in employees:
#     #file.write(employee + " ")
#     file.write("\n" + employee)    
#   print(f"txt file '{file_path}'was created")

# except FileExistsError:
#    print("That file already exists")

#######################################
# JSON format type file wrtiting...
   
# import json 
# employee = {
#   "name": "Shekar",
#   "age": 62,
#   "job": "Cook"
# }

# file_path = "C:/Users/oracl/Desktop/test/output.json"

# try:
#  with open(file_path, "w") as file:
#    json.dump(employee, file, indent=4) # json module use the dump() method.....the 'dump()' method converts dict of(employee) into json output format
# #   for employee in employees:
#     #file.write(employee + " ")
#     #file.write("\n" + employee)    
#    print(f"json file '{file_path}'was created")
# except FileExistsError:
#    print("That file already exists")
###################################
# csv file format example....

import json
import csv

employees = [["Name","Age","Job"],
             ["vijaya",62,"Consultant"],
             ["Koushik",24,"Data Scientist"],
             ["Latha",50,"Family Analyst"]]

file_path = "C:/Users/oracl/Desktop/test/output.csv"
file_path = "C:/Users/oracl/Desktop/test/output.txt"

try:
 with open(file_path, "w", newline="") as file: # give newline keyword argument to aviod space between each row...
   writer = csv.writer(file)
   for row in employees:
     writer.writerow(row)
   #json.dump(employee, file, indent=4) # json module use the dump() method.....the 'dump()' method converts dict of(employee) into json output format
#   for employee in employees:
    #file.write(employee + " ")
    #file.write("\n" + employee)    
     print(f"csv file '{file_path}'was created")
except FileExistsError:
   print("That file already exists")