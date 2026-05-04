def rotate_bits(n: int, d: int, bits: int = 32) -> int:
    """Rotate bits of an integer left by d positions."""
    d %= bits
    return ((n << d) | (n >> (bits - d))) & ((1 << bits) - 1)


def rotate_right(n: int, d: int, bits: int = 32) -> int:
    """Rotate bits of an integer right by d positions."""
    d %= bits
    return ((n >> d) | (n << (bits - d))) & ((1 << bits) - 1)


if __name__ == "__main__":
    print(rotate_bits(16, 2))
    print(rotate_right(16, 2))
