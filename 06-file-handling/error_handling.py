try:
    first = float(input("First number: "))
    second = float(input("Second number: "))
    print("Result:", first / second)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
