def add(x, y):
    # adds two numbers
    return x + y


def sub(x, y):
    # subtracts two numbers
    return x - y


def mul(x, y):
    # multiplies two numbers
    return x * y


def div(x, y):
    # divides two numbers
    return x / y


def mod(x, y):
    # calculates the modulus
    return x % y


while True:
    # take input from the user
    opp = input("Choose the operator(+, - , *, /, %): ")

    # check if input is one of the five options
    if opp in ('+', '-', '*', '/', '%'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if opp == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif opp == '-':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif opp == '*':
            print(num1, "*", num2, "=", mul(num1, num2))

        elif opp == '/':
            print(num1, "/", num2, "=", div(num1, num2))

        elif opp == '%':
            print(num1, "%", num2, "=", mod(num1, num2))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Please choose an operator")
