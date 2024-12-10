# Solution 1: Basic Approach Using a While Loop

# Import the 'random' module to generate a random number
import random

# Generate a random number between 1 and 100 (inclusive)
secret_number = random.randint(1, 100)

# Initialize a variable to store the player's guess
guess = None

# Start a loop that continues until the correct guess is made
while guess != secret_number:
    # Get the player's guess and convert it to an integer
    guess = int(input("Enter your guess: "))

    # Check if the guess is less than the secret number
    if guess < secret_number:
        print("Too low! Try again.")
    # Check if the guess is greater than the secret number
    elif guess > secret_number:
        print("Too high! Try again.")
    # If the guess is correct, congratulate the player
    else:
        print("Correct! You guessed the number.")
