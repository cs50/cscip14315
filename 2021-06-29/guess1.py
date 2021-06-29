# Demonstrates a command-line argument

import random
import sys

maximum = int(sys.argv[1])

number = random.randint(1, maximum)
guess = int(input(f"I'm thinking of a number between 1 and {maximum}: "))

if number == guess:
    print("Yes!")
else:
    print(f"Nope, it was {number}!")
