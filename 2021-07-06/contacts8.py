import csv

with open("contacts.csv") as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        print(f"Email {row[0]} at {row[1]}")
