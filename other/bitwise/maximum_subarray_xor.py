def maximum_subarray_xor(arr: list[int]) -> int:
    """Find the maximum subarray XOR in a given array."""
    n = len(arr)
    max_xor = 0
    for i in range(n):
        curr_xor = 0
        for j in range(i, n):
            curr_xor ^= arr[j]
            max_xor = max(max_xor, curr_xor)
    return max_xor


if __name__ == "__main__":
    print(maximum_subarray_xor([1, 2, 3, 4]))
    print(maximum_subarray_xor([8, 1, 2, 15, 10, 5]))
