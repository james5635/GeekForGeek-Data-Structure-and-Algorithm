import random


def fisher_yates_shuffle(arr: list) -> list:
    """Shuffle array using Fisher-Yates (Knuth) shuffle algorithm."""
    result = arr[:]
    for i in range(len(result) - 1, 0, -1):
        j = random.randint(0, i)
        result[i], result[j] = result[j], result[i]
    return result


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"Original: {arr}")
    print(f"Shuffled: {fisher_yates_shuffle(arr)}")
