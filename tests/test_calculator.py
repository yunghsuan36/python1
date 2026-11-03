import pytest

from app.calculator import add, average, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(5, 0) == 0


def test_divide():
    assert divide(10, 4) == 2.5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_average():
    assert average([1, 2, 3, 4]) == 2.5


def test_average_single_element():
    assert average([5]) == 5


def test_average_floats():
    assert average([0.1, 0.2, 0.3]) == pytest.approx(0.2)


def test_average_empty_raises():
    with pytest.raises(ValueError):
        average([])
