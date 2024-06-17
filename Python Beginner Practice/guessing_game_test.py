secret_word = "no"
guess_count = 0
guess_limit = 3
out_of_guesses = False
guess = ""


while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Guess the word: ")
        guess_count += 1
        if guess_count == 1:
            print("You have 2 Guesses left!")
        elif guess_count == 2:
            print("You have 1 Guesses left!")
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You have no guesses left. YOU LOSE!!")
else:
    print("You Guess the word. YOU WIN!!!")