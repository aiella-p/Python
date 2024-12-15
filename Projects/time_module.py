# import time
# my_time = int(input("Enter the time in seconds: "))

# for x in range(0, my_time, 5):
#     print(x)
#     time.sleep(0.25)
# print("TIME'S UP")

# ############################
# # Time in reverse order....
# import time
# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time,0, -1):
#     print(x)
#     time.sleep(0.5)
# print("TIME'S UP")

############################
# # Display Digital clock...in seconds 

# import time
# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time,0, -1):
#     seconds = x % 60
#     print (f"00:00:{seconds:02}") # want to add '0' zero pad to the seconds...with two digits
#     time.sleep(1)
# print("TIME'S UP")

############################

# Display Digital clock...in seconds with zero padding.... 

# import time
# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time,0, -1):
#     seconds = x % 60
#     print (f"00:00:{seconds:02}") # want to add '0' zero paddings to the seconds...with two digits
#     time.sleep(1)
# print("TIME'S UP")

#Display Digital clock...in minutes and seconds with zero padding.... 

import time
my_time = int(input("Enter the time in seconds: "))

for x in range(my_time,0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x/3600)
    print (f"{hours:02}:{minutes:02}:{seconds:02}") # want to add '0' zero paddings to the seconds...with two digits
    time.sleep(1)
print("TIME'S UP")