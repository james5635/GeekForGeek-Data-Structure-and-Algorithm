def xor_without_xor(a: int, b: int) -> int:
    """Find XOR of two numbers without using XOR operator."""
    return (a | b) & (~a | ~b)


if __name__ == "__main__":
    print(xor_without_xor(5, 3))
    print(xor_without_xor(7, 7))
    print(xor_without_xor(9, 4))
