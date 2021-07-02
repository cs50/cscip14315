import sys

try:
    height = int(input("Height: "))
except ValueError:
    sys.exit("Invalid height!")

for _ in range(height):
    print("#")
