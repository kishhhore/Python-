import random

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)

# Initialize variables
guess = None
attempts = 0

print("Welcome to the Guessing Game!")
print("Try to guess the number between 1 and 100.")

# Main game loop
while guess != target_number:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Check if guess is correct, too high, or too low
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it right in {attempts} attempts!")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

