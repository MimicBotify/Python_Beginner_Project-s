# Banking program python Beginner practice
balance = 100

def show_balance():
    print(f"You're balance is ${balance:.2f}")

def deposit():
    global balance
    print(f"You're current balance is ${balance:.2f}")
    print("How much do you want to Deposit")
    depo_amount = float(input("Input amount: "))
    if depo_amount > 0:
        balance += depo_amount
        print(f"Transaction successful\nYou're new balance is ${balance:.2f}")
    else:
        print("Invalid Transaction")
def withdraw():
    global balance
    print(f"You're current balance is ${balance:.2f}")
    print("How much do you want to Withdraw")
    with_amount = float(input("Input amount: "))
    if with_amount <= 0:
        print("Transaction failed! Withdrawal amount must be positive.")
    elif with_amount > balance:
        print("Transaction failed! Insufficient funds.")
    else:
        balance -= with_amount
        print(f"Transaction successful! You're new balance is ${balance:.2f}")
def main():
    server = True
    while server:
        print("Banking Program")
        print("1. Show Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Choose an option from (1-4): ")
        if choice == '1':
            show_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            server = False
        else:
            print("Invalid Option")
    print("Thank you for using me. Have a nice day!")

if __name__ == '__main__':
    main()
