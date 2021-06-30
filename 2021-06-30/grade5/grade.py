def main():
    score = int(input("What's the score? "))
    letter_grade = get_letter_grade(score)
    print(letter_grade)

def get_letter_grade(score):
    if score <= 100:
        if score >= 90:
            return "A"
        if score >= 80:
            return "B"
        if score >= 70:
            return "C"
        if score >= 60:
            return "D"
        if score >= 0:
            return "F"
    return "Invalid"

if __name__ == "__main__":
    main()
