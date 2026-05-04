def binary_representation(n: int) -> str:
    """Return binary representation of a given integer."""
    if n == 0:
        return "0"
    bits = []
    temp = n
    while temp > 0:
        bits.append(str(temp & 1))
        temp >>= 1
    return "".join(reversed(bits))


if __name__ == "__main__":
    print(binary_representation(10))
    print(binary_representation(0))
    print(binary_representation(7))
