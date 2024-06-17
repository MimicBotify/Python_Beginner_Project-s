import random


def guess_number():
    guess_limit = 10
    guess_count = 0
    guessed = ""
    out_of_guesses = False
    random_num = random.randint(1, 100)
    print("Guess the number between 1-100")
    while guessed != random_num and not out_of_guesses:
        guessed = int(input("Guess the number: "))
        guess_count += 1
        if random_num == guessed:
            print("Congratulation! You have guessed the number.")
        elif guess_count > guess_limit:
            out_of_guesses = True
            print("You are out of guesses. YOU LOSE!!!")
        elif guessed > random_num:
            print("Number is too high! Try again.")
        else:
            print("Number is too low! Try again.")


if __name__ == '__main__':
    guess_number()
