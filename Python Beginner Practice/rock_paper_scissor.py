# Rock paper scissor game
import random

def game():
    condition = True
    while condition:
        print("Let's play Rock, Paper, Scissor")
        choice = ["rock", "paper", "scissor"]
        user_choice = input("Choose rock paper or scissor: ").lower()
        brain = random.choice(choice)
        if user_choice not in choice:
            print("Invalid Choice.")
            continue
        print(f"I choose {brain}")
        if brain == user_choice:
            print("It's an tie!")
        elif (brain == "rock" and user_choice == "paper") or \
             (brain == "paper" and user_choice == "scissor") or \
             (brain == "scissor" and user_choice == "rock"):
            print("YOU WIN!!!")
            condition = False
        else:
            print("I WIN!!!")


if __name__ == '__main__':
    game()