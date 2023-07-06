try:
    x = int(input("Enter a number: "))
    result = 100 / x
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError as e:
    print("Error:", e)
    print("Cannot divide by zero.")
else:
    print("No exception occurred.")
finally:
    print("Execution complete.")

