def main():
    score = int(input("What's the score? "))
    letter_grade = get_letter_grade(score)
    print(letter_grade)

def get_letter_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

if __name__ == "__main__":
    main()
