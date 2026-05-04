def print_lcs_lexicographic(s1: str, s2: str) -> list[str]:
    """Print longest common subsequences in lexicographical order."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[m][n]
    result: list[str] = []

    def backtrack(i: int, j: int, current: str) -> None:
        if len(current) == lcs_length:
            result.append(current)
            return
        visited = set()
        for r in range(i, m):
            for c in range(j, n):
                if (
                    s1[r] == s2[c]
                    and s1[r] not in visited
                    and dp[r + 1][c + 1] == lcs_length - len(current)
                ):
                    visited.add(s1[r])
                    backtrack(r + 1, c + 1, current + s1[r])

    backtrack(0, 0, "")
    return sorted(set(result))


if __name__ == "__main__":
    s1 = "abcabcaa"
    s2 = "acbacba"
    lcs_list = print_lcs_lexicographic(s1, s2)
    print(f"LCS list: {lcs_list}")
