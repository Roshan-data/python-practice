# Type casting means converting one data type into another

# Implicit Type Casting (done by Python automatically)
a = 5       # int
b = 2.5     # float

result = a + b  # int + float → float
print("Result (a + b):", result)
print("Type of result:", type(result))

# Explicit Type Casting (you do it manually)
# Converting float to int
num = 9.8
print("Original number:", num)
print("After casting to int:", int(num))  # removes decimal part

# Converting int to float
x = 10
print("Integer x:", x)
print("After casting to float:", float(x))

# Converting string to int
s = "123"
print("String s:", s)
print("After casting to int:", int(s))

# Converting string to float
s2 = "45.67"
print("String s2:", s2)
print("After casting to float:", float(s2))

# Converting number to string
age = 20
age_str = str(age)
print("Converted to string:", age_str)
print("Type:", type(age_str))