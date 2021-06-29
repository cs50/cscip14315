from mario import is_valid_height, build_pyramid


def test_negative_height():
    assert not is_valid_height(-1)
    assert not is_valid_height(-2)
    assert not is_valid_height(-8)
    assert not is_valid_height(-14315)

def test_zero_height():
    assert not is_valid_height(0)

def test_valid_positive_height():
    assert is_valid_height(1)
    assert is_valid_height(2)
    assert is_valid_height(5)
    assert is_valid_height(8)

def test_invalid_positive_height():
    assert not is_valid_height(9)
    assert not is_valid_height(10)
    assert not is_valid_height(50)
    assert not is_valid_height(14315)

def test_build_pyramid():
    assert build_pyramid(1) == "#"
    assert build_pyramid(2) == " #\n##"
    assert build_pyramid(3) == "  #\n ##\n###"
    assert build_pyramid(8) == "       #\n      ##\n     ###\n    ####\n   #####\n  ######\n" \
        + " #######\n########"
