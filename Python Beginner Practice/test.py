import random


def guess_number():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)

    print("Guess the number between 1 and 100!")

    while True:
        try:
            # Get the user's guess
            guess = int(input("Enter your guess: "))

            # Check if the guess is correct
            if guess == random_number:
                print("Congratulations! You guessed the correct number.")
                break
            elif guess < random_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")


# Start the guessing game
if __name__ == "__main__":
    guess_number()
