import csv

with open("contacts.csv") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        print(f"Email {row['name']} at {row['email']}")
