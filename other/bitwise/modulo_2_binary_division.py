def modulo_2_binary_division(dividend: str, divisor: str) -> str:
    """Perform modulo-2 binary division for CRC."""
    len_divisor = len(divisor)
    temp = dividend[:len_divisor]
    for i in range(len_divisor, len(dividend) + 1):
        if temp[0] == "1":
            temp = format(int(temp, 2) ^ int(divisor, 2), f"0{len(temp)}b")
        if i < len(dividend):
            temp = temp[1:] + dividend[i]
        else:
            temp = temp[1:]
    return temp


if __name__ == "__main__":
    print(modulo_2_binary_division("1101011011", "1011"))
    print(modulo_2_binary_division("100100", "110"))
