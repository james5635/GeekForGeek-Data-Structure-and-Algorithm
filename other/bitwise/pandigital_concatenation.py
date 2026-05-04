def pandigital_concatenation(arr: list[int]) -> int:
    """Count number of pairs with pandigital concatenation."""

    def is_pandigital(s: str) -> bool:
        if len(s) != 9:
            return False
        return set(s) == set("123456789")

    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if is_pandigital(str(arr[i]) + str(arr[j])) or is_pandigital(
                str(arr[j]) + str(arr[i])
            ):
                count += 1
    return count


if __name__ == "__main__":
    print(pandigital_concatenation([123, 456, 789]))
    print(pandigital_concatenation([12, 345, 6789]))
