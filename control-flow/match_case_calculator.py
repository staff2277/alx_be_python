num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = str(input("Choose the operation (+, -, *, /): "))

results = 0

match operation:
    case "+":
        results = num1 + num2
    case "-":
        results = num1 - num2
    case "/":
        if num2 == 0:
            results = "You can not devide a number by 0"
        else:
            results = num1 / num2
    case "*":
        results = num1 * num2
    case _:
        results = "Enter the correct input"

print(f"The result is {results}.")