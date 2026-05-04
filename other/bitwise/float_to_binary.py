def float_to_binary(num: float, places: int = 10) -> str:
    """Convert floating point number to binary representation."""
    if num < 0:
        return "-" + float_to_binary(-num, places)
    int_part = int(num)
    frac_part = num - int_part
    int_binary = bin(int_part)[2:]
    frac_binary = ""
    for _ in range(places):
        frac_part *= 2
        frac_bit = int(frac_part)
        frac_binary += str(frac_bit)
        frac_part -= frac_bit
    return int_binary + "." + frac_binary


if __name__ == "__main__":
    print(float_to_binary(10.625))
    print(float_to_binary(0.5))
    print(float_to_binary(2.75))
