def count_pairs_common_digit(arr: list[int]) -> int:
    """Count pairs in an array with at least one digit common."""

    def get_digits(n: int) -> set[int]:
        digits = set()
        while n > 0:
            digits.add(n % 10)
            n //= 10
        return digits

    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if get_digits(arr[i]) & get_digits(arr[j]):
                count += 1
    return count


if __name__ == "__main__":
    print(count_pairs_common_digit([10, 12, 24]))
    print(count_pairs_common_digit([12, 23, 34, 45]))
