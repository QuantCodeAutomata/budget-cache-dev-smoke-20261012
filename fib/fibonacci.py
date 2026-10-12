def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (0-indexed, F(0)=0, F(1)=1).

    Args:
        n: Non-negative integer index.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError(f"n must be an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
