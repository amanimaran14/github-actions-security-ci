from app import add_numbers

def test_add_positive():
    assert add_numbers(5, 3) == 8

def test_add_negative():
    assert add_numbers(-1, 1) == 0

def test_add_zero():
    assert add_numbers(0, 0) == 0
