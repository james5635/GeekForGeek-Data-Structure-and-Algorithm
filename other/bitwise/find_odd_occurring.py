def find_odd_occurring(arr: list[int]) -> int:
    """Find the number occurring odd number of times in an array."""
    result = 0
    for num in arr:
        result ^= num
    return result


if __name__ == "__main__":
    print(find_odd_occurring([1, 2, 3, 2, 3, 1, 3]))
    print(find_odd_occurring([5, 7, 2, 7, 5]))
