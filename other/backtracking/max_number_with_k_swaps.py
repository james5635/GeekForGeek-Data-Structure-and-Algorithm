def max_number_with_k_swaps(num: str, k: int) -> str:
    """Find maximum number possible by doing at most k swaps."""
    best = num

    def backtrack(s: str, swaps: int) -> None:
        nonlocal best
        if s > best:
            best = s
        if swaps == 0:
            return
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] < s[j]:
                    new_s = list(s)
                    new_s[i], new_s[j] = new_s[j], new_s[i]
                    backtrack("".join(new_s), swaps - 1)

    backtrack(num, k)
    return best


if __name__ == "__main__":
    num = "129814999"
    k = 4
    print(f"Input: {num}, K: {k}")
    print(f"Output: {max_number_with_k_swaps(num, k)}")
    num = "23423456123534"
    k = 8
    print(f"Input: {num}, K: {k}")
    print(f"Output: {max_number_with_k_swaps(num, k)}")
