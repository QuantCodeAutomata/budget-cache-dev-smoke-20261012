import pytest
from fib import fibonacci


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (10, 55),
    (20, 6765),
])
def test_fibonacci_values(n, expected):
    assert fibonacci(n) == expected


def test_fibonacci_type_error():
    with pytest.raises(TypeError):
        fibonacci(1.5)
    with pytest.raises(TypeError):
        fibonacci("5")
    with pytest.raises(TypeError):
        fibonacci(None)


def test_fibonacci_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)
    with pytest.raises(ValueError):
        fibonacci(-100)
