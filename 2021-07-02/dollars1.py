import re


def main():
    amount = input("Amount: ")
    if validate_amount(amount):
        print("Valid!")
    else:
        print("Invalid!")


def validate_amount(amount):
    return re.search("^\$\d+\.\d\d$", amount)


main()
