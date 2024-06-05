import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Invalid input for square root"

def exponentiate(x, y):
    return x ** y

def calculator():
    print("Welcome to the Advanced Calculator!")
    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Exponentiation")
        print("7. Quit")

        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '6'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        elif choice == '5':
            num1 = float(input("Enter a number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        elif choice == '5':
            result = square_root(num1)
            print(f"Square root of {num1} = {result}")
        elif choice == '6':
            print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")
        else:
            print("Invalid input. Please enter a valid choice.")
        a=input("want to restart: ")
        if a=="yes":
            continue
        elif a=="no":
            print("HAVE A GOOD DAY!!😊")
            break     
calculator()