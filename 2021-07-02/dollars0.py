def main():
    amount = input("Amount: ")
    if validate_amount(amount):
        print("Valid!")
    else:
        print("Invalid!")


def validate_amount(amount):

    if not amount.startswith("$"):
        return False

    if len(amount) < 5:
        return False

    if not amount[-1].isdigit() or not amount[-2].isdigit():
        return False

    if amount[-3] != ".":
        return False

    if not amount[1:-3].isdigit():
        return False

    return True


main()
