def longest_sequence_1s_with_flip(n: int) -> int:
    """Find longest sequence of 1s in binary representation with one flip allowed."""
    if n == 0:
        return 1
    prev_len = 0
    curr_len = 0
    max_len = 0
    while n > 0:
        if n & 1:
            curr_len += 1
            max_len = max(max_len, prev_len + 1 + curr_len)
        else:
            prev_len = curr_len
            curr_len = 0
        n >>= 1
    return max_len


if __name__ == "__main__":
    print(longest_sequence_1s_with_flip(13))
    print(longest_sequence_1s_with_flip(1775))
