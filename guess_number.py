import random

# Function to start a new guessing game
def start_game():
    """Starts a new number guessing game."""
    print("\nWelcome to the Number Guessing Game!")
    secret_number = random.randint(1, 100)  # The computer randomly selects a number between 1 and 100
    attempts = 0  # Keeps track of the number of attempts the player has made

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))  # Prompt the player to make a guess
            attempts += 1  # Increment the number of attempts
            if guess < secret_number:
                print("Too low! Try again.")  # Provide a hint if the guess is too low
            elif guess > secret_number:
                print("Too high! Try again.")  # Provide a hint if the guess is too high
            else:
                print(f"Congratulations! You've guessed the correct number in {attempts} attempts.")  # Player guessed correctly
                break  # Exit the game loop
        except ValueError:
            print("Invalid input. Please enter a valid number.")  # Handle non-numeric inputs

# Main program loop
while True:
    print("\nGame Menu:")
    print("1. Start a new game")
    print("2. Exit")
    user_choice = input("Choose an option: ")

    if user_choice == '1':
        start_game()
    elif user_choice == '2':
        print("Thanks for playing! Goodbye!")  # Exit the program
        break
    else:
        print("Invalid selection. Please choose a valid option.")  # Handle invalid menu selections