def booth_multiplication(m: int, q: int, bits: int = 8) -> int:
    """Multiply two numbers using Booth's algorithm."""
    if m < 0:
        m = (1 << bits) + m
    if q < 0:
        q = (1 << bits) + q
    q0 = 0
    a = 0
    for _ in range(bits):
        q0_bit = q & 1
        if q0_bit == 0 and (q0 == 1):
            a = (a + m) & ((1 << bits) - 1)
        elif q0_bit == 1 and (q0 == 0):
            a = (a - m) & ((1 << bits) - 1)
        q0 = q0_bit
        q = (q >> 1) | ((a & 1) << (bits - 1))
        a >>= 1
    return q


if __name__ == "__main__":
    print(booth_multiplication(5, 3))
    print(booth_multiplication(7, 4))
