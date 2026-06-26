"""
PROBLEM STATEMENT:
Write a program to Create number guessing game.
"""

import random

def number_guessing_game():

    """Runs a number guessing game where the user tries to guess a random number.
       This function generates a secret number between 1 and 100, then guides the
       user to the correct answer by providing 'too high' or 'too low' hints.
       The time complexity of each guess check is O(1)."""
    
    secret_number = random.randint(1, 100)
    
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    while True:
    
        try:
        
            guess = int(input("Enter your guess: "))
            
            attempts += 1
            
            if guess < secret_number:
            
                print("Too low! Try again.")
                
            elif guess > secret_number:
            
                print("Too high! Try again.")
                
            else:
            
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                
                break
                
        except ValueError:
        
            print("Invalid input. Please enter a valid integer.")

number_guessing_game()