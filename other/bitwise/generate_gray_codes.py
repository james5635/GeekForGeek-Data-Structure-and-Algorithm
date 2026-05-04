def generate_gray_codes(n: int) -> list[str]:
    """Generate n-bit Gray codes."""
    if n == 0:
        return [""]
    gray_codes = []
    for i in range(1 << n):
        gray = i ^ (i >> 1)
        gray_codes.append(format(gray, f"0{n}b"))
    return gray_codes


if __name__ == "__main__":
    print(generate_gray_codes(2))
    print(generate_gray_codes(3))
