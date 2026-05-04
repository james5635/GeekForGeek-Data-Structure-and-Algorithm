def print_palindromic_partitions(s: str) -> list[list[str]]:
    """Print all palindromic partitions of a string."""

    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]

    def backtrack(idx: int, current: list[str]) -> None:
        if idx == len(s):
            result.append(current[:])
            return
        for i in range(idx + 1, len(s) + 1):
            sub = s[idx:i]
            if is_palindrome(sub):
                current.append(sub)
                backtrack(i, current)
                current.pop()

    result: list[list[str]] = []
    backtrack(0, [])
    return result


if __name__ == "__main__":
    s = "aab"
    partitions = print_palindromic_partitions(s)
    for p in partitions:
        print(p)
