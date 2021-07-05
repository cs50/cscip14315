csvfile = open("contacts.csv")
contents = csvfile.read()
csvfile.close()

rows = contents.splitlines()

for row in rows:
    columns = row.split(",")
    name = columns[0]
    email = columns[1]
    print(f"Email {name} at {email}")
