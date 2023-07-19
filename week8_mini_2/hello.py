add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b if b != 0 else None

def calculate(result=0.0):
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Use the current result for further calculations")
    print("6. Quit")

    choice = input("Enter your choice (1-6): ")

    if choice == '6':
        print("Final result:", result)
        print("Calculator quitting...")
        return

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        operation = None
        if choice == '1':
            operation = add
        elif choice == '2':
            operation = subtract
        elif choice == '3':
            operation = multiply
        elif choice == '4':
            operation = divide

        if operation is not None:
            result = operation(num1, num2)
            if result is not None:
                print("Result:", result)
    elif choice == '5':
        num = float(input("Enter the next number: "))
        result = add(result, num)
        print("Result:", result)
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

    calculate(result)
calculate()