# Python reading files...(.txt,.json and .csv)

# file_path = "C:/Users/oracl/Desktop/test/output.txt"
# with open(file_path, "r") as file: # the open function will return file object we name it as file..
#     content = file.read()
#     print(content) 

############################
# FileNotFoundError.....

# try:
#  file_path = "C:/Users/oracl/Desktop/test/output"
#  with open(file_path, "r") as file: # the open function will return file object we name it as file..
#     content = file.read()
#     print(content) 
# except FileNotFoundError:
#   print("That file was not found") # bcoz we gave file name as output without .txt purposly 

####################################
# PermissionError  

# file_path = "C:/Users/oracl/Desktop/test/output.txt"

# try:
#  file_path = "C:/Users/oracl/Desktop/test/output.txt"
#  with open(file_path, "r") as file: # the open function will return file object we name it as file..
#     content = file.read()
#     print(content) 
# except FileNotFoundError:
#   print("That file was not found") # bcoz we gave file name as output without .txt purposly 

# except FileNotFoundError:
#   print("That file was not found") # bcoz we gave file name as output without .txt purposly 

  #############################################
  # Reading the json files...
# import json

# file_path = "C:/Users/oracl/Desktop/test/output.json"
# file_path = "C:/Users/oracl/Desktop/test/output.csv"

# try:
#  #file_path = "C:/Users/oracl/Desktop/test/output.txt"
#  with open(file_path, "r") as file: # the open function will return file object we name it as file..
#     content = json.load(file) # json module with load method
#     print(content["job"]) 
# except FileNotFoundError:
#   print("That file was not found") # bcoz we gave file name as output without .txt purposly 

# except FileNotFoundError:
#   print("That file was not found") # bcoz we gave file name as output without .txt purposly 

####################################
# reading csv file format...

#import json
import csv

#file_path = "C:/Users/oracl/Desktop/test/output.json"
file_path = "C:/Users/oracl/Desktop/test/output.csv"

try:
 #file_path = "C:/Users/oracl/Desktop/test/output.txt"
 with open(file_path, "r") as file: # the open function will return file object we name it as file..
 #   content = json.load(file) # json module with load method
    content = csv.reader(file)
    for line in content:
     # print(line) 
      #print(line[0]) # To access the specific columns...Here to access first column of csv file
      print(line[1:]) # To access second column of csv till end....

except FileNotFoundError:
  print("That file was not found") # bcoz we gave file name as output without .txt purposly 

except FileNotFoundError:
  print("That file was not found") # bcoz we gave file name as output without .txt purposly 

  
