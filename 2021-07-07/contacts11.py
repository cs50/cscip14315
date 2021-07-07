import csv
import sys


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    people = load_people(sys.argv[1])

    for person in people:
        print(f"Email {person.name} at {person.email}")


def load_people(filename):
    people = []
    with open(filename) as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            person = Person(row["name"], row["email"])
            people.append(person)
    return people


main()
