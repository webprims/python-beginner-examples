first = float(input("First number: "))
operator = input("Choose +, -, *, or /: ")
second = float(input("Second number: "))

if operator == "+":
    result = first + second
elif operator == "-":
    result = first - second
elif operator == "*":
    result = first * second
elif operator == "/":
    if second == 0:
        print("Cannot divide by zero.")
        raise SystemExit
    result = first / second
else:
    print("Unknown operator.")
    raise SystemExit

print("Result:", result)
