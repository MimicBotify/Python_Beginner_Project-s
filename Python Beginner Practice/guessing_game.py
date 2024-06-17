
secret_word = "cup"
guess = ""
guessing_count = 0
guessing_limit = 3
out_of_guesses = False
while guess != secret_word and not out_of_guesses:
    if guessing_count < guessing_limit:
        guess = input("Guess the word: ")
        guessing_count += 1
        if guessing_count == 1:
            print("You have 2 Guesses left")
        elif guessing_count == 2:
            print("You have 1 Guesses left")
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You are out of guesses. YOU LOSE!")
else:
    print("You WIN!!!")
     