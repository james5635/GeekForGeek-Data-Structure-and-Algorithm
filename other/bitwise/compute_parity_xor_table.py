def compute_parity_xor_table(n: int) -> int:
    """Compute parity of a number using XOR table look-up."""
    if n <= 0xFFFF:
        table = [0] * 65536
        for i in range(65536):
            table[i] = (i & 1) ^ table[i >> 1]
        return table[n]
    n ^= n >> 16
    n ^= n >> 8
    n ^= n >> 4
    n ^= n >> 2
    n ^= n >> 1
    return n & 1


if __name__ == "__main__":
    print(compute_parity_xor_table(5))
    print(compute_parity_xor_table(7))
    print(compute_parity_xor_table(11))
