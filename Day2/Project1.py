# Simple Calculator Program

print("Welcome to the Python Calculator!")
print("Select an operation: +, -, *, /, %, **, //")

# Taking input from user
num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))

# Performing calculation based on operator
if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
elif operator == "%":
    print("Result:", num1 % num2)
elif operator == "**":
    print("Result:", num1 ** num2)
elif operator == "//":
    print("Result:", num1 // num2)
else:
    print("Invalid operator!")