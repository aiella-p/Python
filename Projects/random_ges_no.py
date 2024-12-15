# Explanation:

# Uses a while loop to repeatedly prompt the player for their guess until they guess correctly.
# The random.randint(1, 100) function generates a random number between 1 and 100.
# After each guess, the program checks if the guess is too low, too high, or correct and provides appropriate feedback.
# This approach is simple and effective, using a loop for repeated guesses.
# Solution 2: Using a Function and Recursion

# Solution 2: Using a Function and Recursion

# Import the 'random' module to generate a random number
import random

# Generate a random number between 1 and 100 (inclusive)
secret_number = random.randint(1, 100)

# Define a function to handle the guessing logic
def guess_number():
    """Recursive function to guess the number."""
    # Get the player's guess and convert it to an integer
    guess = int(input("Enter your guess: "))

    # Check if the guess is less than the secret number
    if guess < secret_number:
        print("Too low! Try again.")
        # Call the function recursively to ask for another guess
        guess_number()
    # Check if the guess is greater than the secret number
    elif guess > secret_number:
        print("Too high! Try again.")
        # Call the function recursively to ask for another guess
        guess_number()
    # If the guess is correct, congratulate the player
    else:
        print("Correct! You guessed the number.")

# Start the guessing game by calling the function
guess_number()
