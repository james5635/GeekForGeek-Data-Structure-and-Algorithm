def square_without_operators(n: int) -> int:
    """Calculate square of a number without using *, / and pow()."""
    if n == 0:
        return 0
    if n < 0:
        n = -n
    if n & 1:
        return (square_without_operators(n >> 1) << 2) + (n << 1) - 1
    else:
        return square_without_operators(n >> 1) << 2


if __name__ == "__main__":
    print(square_without_operators(5))
    print(square_without_operators(7))
    print(square_without_operators(10))
