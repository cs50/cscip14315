# Demonstrates a list

import random
import sys

colors = ["red", "yellow", "blue"]

index = random.randint(1, len(colors))
color = colors[index - 1]
guess = input(f"I'm thinking of a color: ")

if color == guess:
    print("Yes!")
else:
    print(f"Nope, it was {color}!")
