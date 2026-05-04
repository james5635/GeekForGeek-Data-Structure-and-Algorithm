def find_two_non_repeating(arr: list[int]) -> tuple[int, int]:
    """Find two non-repeating elements in an array of repeating elements."""
    xor_all = 0
    for num in arr:
        xor_all ^= num
    rightmost_set = xor_all & -xor_all
    x, y = 0, 0
    for num in arr:
        if num & rightmost_set:
            x ^= num
        else:
            y ^= num
    return x, y


if __name__ == "__main__":
    print(find_two_non_repeating([2, 3, 7, 9, 11, 2, 3, 11]))
    print(find_two_non_repeating([5, 7, 5, 7, 8, 9]))
