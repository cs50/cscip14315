from grade import get_letter_grade


def test_90_and_above():
    assert get_letter_grade(90) == "A"
    assert get_letter_grade(92) == "A"
    assert get_letter_grade(95) == "A"
    assert get_letter_grade(99) == "A"
    assert get_letter_grade(100) == "A"
