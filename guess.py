# Demonstrates importing a module

import random

number = random.randint(1, 10)
guess = int(input("I'm thinking of a number between 1 and 10: "))

if number == guess:
    print("Yes!")
else:
    print(f"Nope, it was {number}!")
