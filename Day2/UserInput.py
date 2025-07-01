# Taking user input using input() function

# Asking for user's name
name = input("Enter your name: ")
print("My name is "+name)

# Asking user for their age
age = input("How old are you? ")
print("You are " + age + " years old")

# Asking two numbers and adding them
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert to int before adding
num1 = int(num1)
num2 = int(num2)

total = num1 + num2
print("The total is", total)