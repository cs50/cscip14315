with open("contacts.csv") as csvfile:
    rows = csvfile.read().splitlines()

for row in rows:
    columns = row.split(",")
    print(f"Email {columns[0]} at {columns[1]}")
