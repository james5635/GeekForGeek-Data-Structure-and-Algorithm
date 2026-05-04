def check_integer_overflow(a: int, b: int, bits: int = 32) -> tuple[bool, bool]:
    """Check for integer overflow when adding two numbers. Returns (overflow, underflow)."""
    max_val = (1 << (bits - 1)) - 1
    min_val = -(1 << (bits - 1))
    result = a + b
    overflow = result > max_val
    underflow = result < min_val
    return overflow, underflow


if __name__ == "__main__":
    print(check_integer_overflow(2147483647, 1))
    print(check_integer_overflow(-2147483648, -1))
    print(check_integer_overflow(100, 200))
