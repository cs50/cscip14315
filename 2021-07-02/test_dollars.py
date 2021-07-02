from dollars import validate_amount

def test_dollar_sign():
    assert validate_amount("$1.23") == True
    assert validate_amount("1.23") == False

def test_length():
    assert validate_amount("") == False
    assert validate_amount("1") == False
    assert validate_amount("12") == False
    assert validate_amount("123") == False
    assert validate_amount("123") == False
    assert validate_amount("1.23") == True
    assert validate_amount("12.34") == True
