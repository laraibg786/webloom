"""Tests for webloom.utils module."""

import pytest

from webloom.utils import add_numbers, fibonacci, is_even, multiply_numbers


class TestAddNumbers:
    """Test cases for add_numbers function."""

    def test_positive_numbers(self):
        """Test adding positive numbers."""
        assert add_numbers(1, 2) == 3
        assert add_numbers(10, 20) == 30

    def test_negative_numbers(self):
        """Test adding negative numbers."""
        assert add_numbers(-1, -2) == -3
        assert add_numbers(-5, 5) == 0

    def test_zero(self):
        """Test adding with zero."""
        assert add_numbers(0, 5) == 5
        assert add_numbers(5, 0) == 5


class TestMultiplyNumbers:
    """Test cases for multiply_numbers function."""

    def test_basic_multiplication(self):
        """Test basic multiplication."""
        assert multiply_numbers(2, 3) == 6
        assert multiply_numbers(5, 4) == 20

    def test_with_zero(self):
        """Test multiplication with zero."""
        assert multiply_numbers(0, 5) == 0
        assert multiply_numbers(5, 0) == 0

    def test_negative_numbers(self):
        """Test multiplication with negative numbers."""
        assert multiply_numbers(-2, 3) == -6
        assert multiply_numbers(-2, -3) == 6


class TestIsEven:
    """Test cases for is_even function."""

    def test_even_numbers(self):
        """Test even numbers."""
        assert is_even(0) is True
        assert is_even(2) is True
        assert is_even(100) is True

    def test_odd_numbers(self):
        """Test odd numbers."""
        assert is_even(1) is False
        assert is_even(3) is False
        assert is_even(99) is False

    def test_negative_even(self):
        """Test negative even numbers."""
        assert is_even(-2) is True
        assert is_even(-4) is True


class TestFibonacci:
    """Test cases for fibonacci function."""

    def test_base_cases(self):
        """Test base cases."""
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1

    def test_small_values(self):
        """Test small Fibonacci numbers."""
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(4) == 3
        assert fibonacci(5) == 5
        assert fibonacci(6) == 8

    def test_larger_value(self):
        """Test a larger Fibonacci number."""
        assert fibonacci(10) == 55
        assert fibonacci(15) == 610

    def test_negative_raises_error(self):
        """Test that negative n raises ValueError."""
        with pytest.raises(ValueError, match="n must be non-negative"):
            fibonacci(-1)
