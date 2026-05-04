def gcd_bitwise(a: int, b: int) -> int:
    """Euclid's algorithm using bitwise operators when / and * are costly."""
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a & 1 == 0 and b & 1 == 0:
        return gcd_bitwise(a >> 1, b >> 1) << 1
    elif a & 1 == 0:
        return gcd_bitwise(a >> 1, b)
    elif b & 1 == 0:
        return gcd_bitwise(a, b >> 1)
    elif a > b:
        return gcd_bitwise((a - b) >> 1, b)
    else:
        return gcd_bitwise((b - a) >> 1, a)


if __name__ == "__main__":
    print(gcd_bitwise(12, 8))
    print(gcd_bitwise(15, 10))
    print(gcd_bitwise(18, 24))
