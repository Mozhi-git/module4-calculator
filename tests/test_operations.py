import pytest
from app.operation import Operation


def test_add():
    assert Operation.add(5, 3) == 8

def test_subtract():
    assert Operation.subtract(10, 4) == 6

def test_multiply():
    assert Operation.multiply(6, 4) == 24

def test_divide():
    assert Operation.divide(20, 4) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        Operation.divide(20, 0)