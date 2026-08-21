import random

secret_number = random.randint(1, 10)

print("Guess a number between 1 and 10.")

while True:
    guess = int(input("Your guess: "))

    if guess == secret_number:
        print("Correct! Well done.")
        break
    if guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
