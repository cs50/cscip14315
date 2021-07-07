import csv


class Scrabble:

    _points = {}

    def __init__(self):
        with open("scrabble.csv") as csvfile:
            rows = csv.DictReader(csvfile)
            for row in rows:
                letter = row["letters"]
                points = int(row["points"])
                self._points[letter] = points

    def play(self, word1, word2):
        score1 = self._calculate_score(word1)
        score2 = self._calculate_score(word2)
        if score1 > score2:
            print("Player 1 wins!")
        elif score1 < score2:
            print("Player 2 wins!")
        else:
            print("It's a tie!")

    def _calculate_score(self, word):
        score = 0
        for character in word.upper():
            if character in self._points:
                score += self._points[character]
        return score


def main():

    scrabble = Scrabble()

    word1 = input("Player 1: ")
    word2 = input("Player 2: ")

    scrabble.play(word1, word2)


main()
