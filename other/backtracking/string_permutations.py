def find_permutations(s: str) -> list[str]:
    """Return all permutations of a given string."""

    def backtrack(path: str, remaining: str) -> None:
        if not remaining:
            result.append(path)
            return
        for i in range(len(remaining)):
            backtrack(path + remaining[i], remaining[:i] + remaining[i + 1 :])

    result: list[str] = []
    backtrack("", s)
    return result


if __name__ == "__main__":
    s = "ABC"
    perms = find_permutations(s)
    for p in perms:
        print(p)
