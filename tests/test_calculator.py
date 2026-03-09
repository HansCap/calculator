"""Unit tests for calculator functions."""

import sys
import pytest
from pathlib import Path

# Add src directory to path to import calculator module
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from calculator import add, subtract, multiply, divide, power, modulo


class TestAdd:
    """Test cases for the add function."""

    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_zero(self):
        assert add(-1, 1) == 0

    def test_add_negative_numbers(self):
        assert add(-5, -3) == -8

    def test_add_zeros(self):
        assert add(0, 0) == 0

    def test_add_floats(self):
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    """Test cases for the subtract function."""

    def test_subtract_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_subtract_same_numbers(self):
        assert subtract(1, 1) == 0

    def test_subtract_negative_numbers(self):
        assert subtract(-5, -3) == -2

    def test_subtract_from_zero(self):
        assert subtract(0, 5) == -5

    def test_subtract_floats(self):
        assert subtract(10.5, 2.5) == 8.0


class TestMultiply:
    """Test cases for the multiply function."""

    def test_multiply_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_multiply_negative_and_positive(self):
        assert multiply(-2, 5) == -10

    def test_multiply_negative_numbers(self):
        assert multiply(-3, -4) == 12

    def test_multiply_by_zero(self):
        assert multiply(0, 100) == 0

    def test_multiply_floats(self):
        assert multiply(2.5, 4) == 10.0


class TestDivide:
    """Test cases for the divide function."""

    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5

    def test_divide_with_remainder(self):
        assert divide(7, 2) == 3.5

    def test_divide_negative_by_positive(self):
        assert divide(-10, 2) == -5

    def test_divide_negative_numbers(self):
        assert divide(-10, -2) == 5

    def test_divide_zero(self):
        assert divide(0, 5) == 0

    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError):
            divide(10, 0)


class TestModulo:
    """Test cases for the modulo function."""

    def test_modulo_basic(self):
        assert modulo(10, 3) == 1

    def test_modulo_no_remainder(self):
        assert modulo(10, 5) == 0

    def test_modulo_negative_dividend(self):
        assert modulo(-10, 3) == 2

    def test_modulo_negative_divisor(self):
        assert modulo(10, -3) == -2

    def test_modulo_by_zero_raises_error(self):
        with pytest.raises(ValueError):
            modulo(10, 0)
