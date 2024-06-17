guess = ""
secret_word = "tanvir"
guess_count = 0
guess_limit = 5
limit_reach = False

while guess != secret_word and not limit_reach:
    if guess_count < guess_limit:
        guess = input("Guess the Word: ")
        guess_count += 1
        if guess_count == 1:
            print("You have 4 Guesses left")
        elif guess_count == 2:
            print("You have 3 Guesses left")
        elif guess_count == 3:
            print("You have 2 Guesses left")
        elif guess_count == 2:
            print("This is your last Guess")
    else:
        limit_reach = True
if limit_reach:
    print("You are out of Guesses\nYou LOSE!!!")
else:
    print("Congrats!!! You guessed the word.")