import random


def randomized_binary_search(
    arr: list[int], target: int, left: int = 0, right: int | None = None
) -> int:
    """Binary search that selects a random pivot within the valid range."""
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1

    pivot = random.randint(left, right)

    if arr[pivot] == target:
        return pivot
    elif arr[pivot] > target:
        return randomized_binary_search(arr, target, left, pivot - 1)
    else:
        return randomized_binary_search(arr, target, pivot + 1, right)


if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target = 12
    idx = randomized_binary_search(arr, target)
    print(f"Array: {arr}")
    print(f"Target: {target}, Found at index: {idx}")
