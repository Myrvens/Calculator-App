def add(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}\n")

def sub(a, b):
    answer = a - b
    print(f"{a} - {b} = {answer}\n")

def mul(a, b):
    answer = a * b
    print(f"{a} * {b} = {answer}\n")

def div(a, b):
    if b != 0:  # Check to avoid division by zero
        answer = a / b
        print(f"{a} / {b} = {answer}\n")
    else:
        print("Division by zero is not allowed.\n")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    
    choice = input("Input your choice: ").strip().lower()

    if choice == "a":
        print("Addition")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        add(a, b)

    elif choice == "b":
        print("Subtraction")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        sub(a, b)

    elif choice == "c":
        print("Multiplication")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        mul(a, b)

    elif choice == "d":
        print("Division")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        div(a, b)

    elif choice == "e":
        print("Exiting the calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.\n")
