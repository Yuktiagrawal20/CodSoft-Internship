def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 'Error! Division by zero is not allowed.'
    else:
        return x / y

def modulus(x, y):
    if y == 0 or not x.is_integer() or not y.is_integer():
        return 'Error! Modulus operation can only be performed on non-zero integers.'
    else:
        return x % y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

operation = input("Enter the number of the operation you want to perform: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == '1':
    print("Result:", add(num1, num2))
elif operation == '2':
    print("Result:", subtract(num1, num2))
elif operation == '3':
    print("Result:", multiply(num1, num2))
elif operation == '4':
    print("Result:", divide(num1, num2))
elif operation == '5':
    print("Result:", modulus(num1, num2))
else:
    print("Invalid operation selection.")
