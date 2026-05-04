def russian_peasant_multiplication(a: int, b: int) -> int:
    """Multiply two numbers using bitwise operators (Russian Peasant method)."""
    result = 0
    while b > 0:
        if b & 1:
            result += a
        a <<= 1
        b >>= 1
    return result


if __name__ == "__main__":
    print(russian_peasant_multiplication(5, 3))
    print(russian_peasant_multiplication(10, 12))
    print(russian_peasant_multiplication(7, 8))
