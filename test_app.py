from app import add, subtract, multiply

def test_add():
    assert add(4,3) == 7

def test_subtract():
    assert subtract(4,3) == 1

def test_multiply():
    assert multiply(4,3) == 12

