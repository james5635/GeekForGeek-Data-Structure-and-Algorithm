def gray_to_binary(gray: int) -> int:
    """Convert Gray code to Binary code."""
    binary = gray
    while gray:
        gray >>= 1
        binary ^= gray
    return binary


def binary_to_gray(binary: int) -> int:
    """Convert Binary code to Gray code."""
    return binary ^ (binary >> 1)


if __name__ == "__main__":
    print(gray_to_binary(4))
    print(binary_to_gray(7))
