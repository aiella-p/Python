email = input("Enter your email: ")

index = email.index("@")

username = email[:index] #starts with username till '@' 
#domain = email[index:] # starts with '@'
domain = email[index + 1:] # To omit the '@' sign during output....!

print(f"Your username is {username} and domain is {domain}")        