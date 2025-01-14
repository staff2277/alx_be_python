def perform_operation(num1, num2, operation):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "You cannot divide a number by zero"
        result = num1 / num2
    else:
        return "Invalid operation"
    
    return f"Result: {result}"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

print(perform_operation(num1, num2, operation))
