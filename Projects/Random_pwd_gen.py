#Random Password Generator Solutions and Explanations
# #Generate a  random password of a specified length.
# Approach using the 'random' Module
# Input values:
# User specifies the desired password length.

# Output value:
# Randomly generated passwords of the specified length.

# Example:

# Input values:
# Enter the desired password length: 12
# Output value:
# Generated password: Xy#7pLm$9oR5

# Solution 1: Basic Approach Using the `random` Module

import random  # Import the random module for random selection of characters

# Function to generate a random password
def generate_password(length):
    # Define possible characters for the password: lowercase, uppercase, digits, and special characters
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    
    # Initialize an empty password string
    password = ""

    # Loop to generate each character of the password
    for _ in range(length):
        # Randomly select a character from the list and append to the password
        password += random.choice(characters)

    return password

# Get user input for the desired password length
password_length = int(input("Enter the desired password length: "))

# Generate the password using the specified length
generated_password = generate_password(password_length)

# Print the generated password
print(f"Generated password: {generated_password}")
