"""Utility functions for Webloom."""


def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b

    Examples:
        >>> add_numbers(1, 2)
        3
        >>> add_numbers(-1, 1)
        0
    """
    return a + b


def multiply_numbers(a: int, b: int) -> int:
    """
    Multiply two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        The product of a and b

    Examples:
        >>> multiply_numbers(2, 3)
        6
        >>> multiply_numbers(0, 5)
        0
    """
    return a * b


def is_even(n: int) -> bool:
    """
    Check if a number is even.

    Args:
        n: The number to check

    Returns:
        True if n is even, False otherwise

    Examples:
        >>> is_even(2)
        True
        >>> is_even(3)
        False
        >>> is_even(0)
        True
    """
    return n % 2 == 0


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.

    Args:
        n: The position in the Fibonacci sequence (0-based)

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(5)
        5
        >>> fibonacci(10)
        55
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
