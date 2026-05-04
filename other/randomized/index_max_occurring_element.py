import random


def index_max_occurring_element(arr: list[int]) -> int:
    """Find index of a maximum occurring element chosen with equal probability among all max occurrences."""
    if not arr:
        raise ValueError("Array cannot be empty")

    max_val = arr[0]
    max_indices = [0]

    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_indices = [i]
        elif arr[i] == max_val:
            max_indices.append(i)

    return random.choice(max_indices)


if __name__ == "__main__":
    arr = [1, 3, 2, 3, 3, 1, 3]
    counts = {i: 0 for i in range(len(arr)) if arr[i] == 3}
    for _ in range(10000):
        idx = index_max_occurring_element(arr)
        counts[idx] = counts.get(idx, 0) + 1
    print(f"Array: {arr}")
    print(f"Selection distribution: {counts}")
