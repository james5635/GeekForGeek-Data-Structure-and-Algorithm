def karatsuba_multiplication(x: int, y: int) -> int:
    """Multiply two numbers using Karatsuba algorithm."""
    if x < 10 or y < 10:
        return x * y
    m = max(len(str(x)), len(str(y)))
    m2 = m // 2
    high1, low1 = divmod(x, 10**m2)
    high2, low2 = divmod(y, 10**m2)
    z0 = karatsuba_multiplication(low1, low2)
    z1 = karatsuba_multiplication((low1 + high1), (low2 + high2))
    z2 = karatsuba_multiplication(high1, high2)
    return (z2 * 10 ** (2 * m2)) + ((z1 - z2 - z0) * 10**m2) + z0


if __name__ == "__main__":
    print(karatsuba_multiplication(1234, 5678))
    print(karatsuba_multiplication(15, 12))
