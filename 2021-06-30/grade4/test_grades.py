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

def test_70_and_above():
    assert get_letter_grade(70) == "C"
    assert get_letter_grade(73) == "C"
    assert get_letter_grade(75) == "C"
    assert get_letter_grade(78) == "C"
    assert get_letter_grade(79) == "C"

def test_60_and_above():
    assert get_letter_grade(60) == "D"
    assert get_letter_grade(63) == "D"
    assert get_letter_grade(65) == "D"
    assert get_letter_grade(68) == "D"
    assert get_letter_grade(69) == "D"

def test_below_60():
    assert get_letter_grade(60) == "D"
    assert get_letter_grade(63) == "D"
    assert get_letter_grade(65) == "D"
    assert get_letter_grade(68) == "D"
    assert get_letter_grade(69) == "D"

def test_invalid_score():
    assert get_letter_grade(-1) == "Invalid"
    assert get_letter_grade(-4) == "Invalid"
    assert get_letter_grade(-5) == "Invalid"
    assert get_letter_grade(-90) == "Invalid"
    assert get_letter_grade(101) == "Invalid"
    assert get_letter_grade(110) == "Invalid"
    assert get_letter_grade(125) == "Invalid"
