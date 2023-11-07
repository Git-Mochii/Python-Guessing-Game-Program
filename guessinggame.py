
# Simple Guessing Game Project #

import random

print("//////////////////////////////// \n")
print("Welcome to the guessing game! \n")
print("//////////////////////////////// \n")

# Function to get difficulty level from the player
def difficulty_modes():
    while True:
        try:
            difficulty = int(input("Input a difficulty (1 for easy, 2 for medium, 3 for hard): "))
            if difficulty in [1, 2, 3]:
                return difficulty
            else:
                print("Invalid. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid. Enter a valid number.")

# Dictionary for difficulty levels (each level is a different range of numbers to guess from)
difficulty_ranges = {1: (1, 50), 2: (1, 100), 3: (1, 200)}

difficulty = difficulty_modes()
min_range, max_range = difficulty_ranges[difficulty]

print(f"You are now playing on difficulty {difficulty}. Guess between {min_range} and {max_range}.")

hidden_num = random.randint(min_range, max_range)

attempt = 0 # Number of attempts
guess = None # User guess input

while guess != hidden_num: # Continue the loop until the user guesses the correct number
    try:
        guess = int(input(f"Guess between {min_range} and {max_range}: ")) # User input prompt
        attempt += 1 # Increment attempts

        if guess < hidden_num: # If the guess is less than the hidden number, provide a hint
            print("Try a higher number.")
        elif guess > hidden_num: # If the guess is greater than the hidden number, provide a hint
            print("Try a lower number")
        else: 
            print(f"Well done! You guess the number {hidden_num}. You guessed the number within {attempt} attempts.") # User input correct
    except ValueError:
        print("Invalid input. Enter a valid number.") # User input invalid

