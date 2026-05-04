def add_bit_strings(a: str, b: str) -> str:
    """Add two bit strings and return the result as a bit string."""
    result = ""
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 or j >= 0 or carry:
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0
        total = bit_a + bit_b + carry
        result = str(total & 1) + result
        carry = total >> 1
        i -= 1
        j -= 1
    return result


if __name__ == "__main__":
    print(add_bit_strings("1101", "1011"))
    print(add_bit_strings("10", "01"))
    print(add_bit_strings("111", "111"))
