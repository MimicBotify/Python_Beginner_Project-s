num1 = float(input("Input First Number: "))
operator = input("Input Operator:")
num2 = float(input("Input Second Number: "))


def calculate():
    while num1 != "off":
        if operator == "+":
            print(num1 + num2)
        elif operator == "-":
            print(num1 - num2)
        elif operator == "/":
            print(num1 / num2)
        elif operator == "*":
            print(num1 * num2)
        else:
            print("Input the valid operator")


calculate()