from grade import get_letter_grade


def test_90_and_above():
    assert get_letter_grade(90) == "A"
    assert get_letter_grade(92) == "A"
    assert get_letter_grade(95) == "A"
    assert get_letter_grade(99) == "A"
    assert get_letter_grade(100) == "A"

def test_80_and_above():
    assert get_letter_grade(80) == "B"
    assert get_letter_grade(83) == "B"
    assert get_letter_grade(85) == "B"
    assert get_letter_grade(88) == "B"
    assert get_letter_grade(89) == "B"
