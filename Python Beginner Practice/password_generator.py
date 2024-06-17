# Strong password generator
import random
import os


def password_generator():
    character = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                 "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                 "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                 "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-",
                 ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^",
                 "_", "`", "{", "|", "}", "~"]

    first_digit = random.choice(character)
    second_digit = random.choice(character)
    third_digit = random.choice(character)
    forth_digit = random.choice(character)
    fifth_digit = random.choice(character)
    six_digit = random.choice(character)
    seven_digit = random.choice(character)
    eight_digit = random.choice(character)

    user_int = float(input("Enter the number of your password length from (4-8): "))
    try:
        if user_int == 4:
            password = (first_digit + second_digit + third_digit + forth_digit)
            print(password)
            return password
        elif user_int == 5:
            password = (first_digit + second_digit + third_digit + forth_digit + fifth_digit)
            print(password)
            return password
        elif user_int == 6:
            password = (first_digit + second_digit + third_digit + forth_digit + fifth_digit + six_digit)
            print(password)
            return password
        elif user_int == 7:
            password = (first_digit + second_digit + third_digit + forth_digit + fifth_digit + six_digit + seven_digit)
            print(password)
            return password
        elif user_int == 8:
            password = (first_digit + second_digit + third_digit + forth_digit + fifth_digit + six_digit + seven_digit + eight_digit)
            print(password)
            return password
        else:
            print("Invalid Input")
            password_generator()
    except ValueError:
        print("Try Again! Choose from(4-8)")
        password_generator()


def save_password():
    pass_path = "C:\\Users\\DELL\\OneDrive\\Desktop\\Python Beginner Practice\\Password's\\password.txt"
    output_password = password_generator()
    if not os.path.exists(pass_path):
        with open(pass_path, "w") as file:
            file.write("")
        with open(pass_path, "a") as file:
            file_content = output_password
            file.write(file_content + "\n")
            print("Password Saved Successfully.")
    else:
        with open(pass_path, "a") as file:
            file_content = output_password
            file.write(file_content + "\n")
            print("Password Saved Successfully.")


if __name__ == '__main__':
    save_password()
