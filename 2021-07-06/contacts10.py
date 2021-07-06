import csv
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1]) as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            print(f"Email {row['name']} at {row['email']}")
except FileNotFoundError:
    sys.exit("File not found")
