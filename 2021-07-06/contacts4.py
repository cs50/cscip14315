people = [
    {"name": "David", "email": "malan@harvard.edu"},
    {"name": "Kareem", "email": "kzidane@cs50.harvard.edu"},
    {"name": "Carter", "email": "carter@cs50.harvard.edu"}
]

for i in range(3):
    person = people[i]
    name = person["name"]
    email = person["email"]
    print(f"Email {name} at {email}")
