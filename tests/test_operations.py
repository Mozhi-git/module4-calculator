import pytest

from app.operation import Operation


@pytest.mark.parametrize(
    "operation, a, b, expected",
    [
        (Operation.add, 5, 3, 8),
        (Operation.subtract, 10, 4, 6),
        (Operation.multiply, 6, 4, 24),
        (Operation.divide, 20, 4, 5.0),
    ],
)
def test_operations(operation, a, b, expected):
    assert operation(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError):
        Operation.divide(20, 0)