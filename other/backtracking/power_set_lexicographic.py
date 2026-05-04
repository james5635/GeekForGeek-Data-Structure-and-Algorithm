def power_set_lexicographic(s: str) -> list[str]:
    """Generate power set of a string in lexicographic order."""
    s = sorted(s)
    result: list[str] = []

    def backtrack(idx: int, current: str) -> None:
        if current:
            result.append(current)
        for i in range(idx, len(s)):
            if i > idx and s[i] == s[i - 1]:
                continue
            backtrack(i + 1, current + s[i])

    backtrack(0, "")
    result.sort()
    return result


if __name__ == "__main__":
    s = "abc"
    subsets = power_set_lexicographic(s)
    for subset in subsets:
        print(subset)
