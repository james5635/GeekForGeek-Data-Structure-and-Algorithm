"""
Edit Distance (Levenshtein Distance) - Dynamic Programming
Source: https://www.geeksforgeeks.org/dsa/edit-distance-dp-5/

Given two strings s1 and s2, find the minimum number of operations to convert s1 to s2.
Allowed operations (all with equal cost):
- Insert: Insert any character
- Remove: Remove a character
- Replace: Replace a character with another

Time Complexity: O(m * n) where m and n are lengths of the two strings
Space Complexity: O(m * n) for the DP table (or O(n) for space-optimized version)
"""


def edit_distance(s1: str, s2: str) -> int:
    """
    Find the minimum edit distance between two strings using
    bottom-up dynamic programming (tabulation).

    Args:
        s1: Source string
        s2: Target string

    Returns:
        Minimum number of operations to convert s1 to s2
    """
    m = len(s1)
    n = len(s2)

    # Create DP table of size (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill base cases
    # If s1 is empty, need to insert all characters of s2
    for j in range(n + 1):
        dp[0][j] = j
    # If s2 is empty, need to remove all characters of s1
    for i in range(m + 1):
        dp[i][0] = i

    # Fill the rest of the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],  # Insert
                    dp[i - 1][j],  # Remove
                    dp[i - 1][j - 1],  # Replace
                )

    return dp[m][n]


def edit_distance_space_optimized(s1: str, s2: str) -> int:
    """
    Space-optimized version using two 1D arrays.
    Reduces space complexity from O(m*n) to O(n).

    Args:
        s1: Source string
        s2: Target string

    Returns:
        Minimum number of operations to convert s1 to s2
    """
    m = len(s1)
    n = len(s2)

    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    # Initialize for 0-th row
    for j in range(n + 1):
        prev[j] = j

    # Fill the rest of the rows
    for i in range(1, m + 1):
        curr[0] = i
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(
                    curr[j - 1],  # Insert
                    prev[j],  # Remove
                    prev[j - 1],  # Replace
                )
        prev = curr[:]

    return prev[n]


def edit_distance_single_array(s1: str, s2: str) -> int:
    """
    Further space-optimized version using a single 1D array.

    Args:
        s1: Source string
        s2: Target string

    Returns:
        Minimum number of operations to convert s1 to s2
    """
    m = len(s1)
    n = len(s2)

    curr = [0] * (n + 1)

    # Initialize
    for j in range(n + 1):
        curr[j] = j

    for i in range(1, m + 1):
        prev = curr[0]
        curr[0] = i
        for j in range(1, n + 1):
            temp = curr[j]
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev
            else:
                curr[j] = 1 + min(curr[j - 1], prev, curr[j])
            prev = temp

    return curr[n]


if __name__ == "__main__":
    # Test case 1
    s1, s2 = "geek", "gesek"
    print(f"s1 = '{s1}', s2 = '{s2}'")
    print(f"Edit distance: {edit_distance(s1, s2)}")  # Expected: 1
    print()

    # Test case 2
    s1, s2 = "gfg", "gfg"
    print(f"s1 = '{s1}', s2 = '{s2}'")
    print(f"Edit distance: {edit_distance(s1, s2)}")  # Expected: 0
    print()

    # Test case 3
    s1, s2 = "abcd", "bcfe"
    print(f"s1 = '{s1}', s2 = '{s2}'")
    print(f"Edit distance: {edit_distance(s1, s2)}")  # Expected: 3
    print()

    # Test case 4
    s1, s2 = "GEEXSFRGEEKKS", "GEEKSFORGEEKS"
    print(f"s1 = '{s1}', s2 = '{s2}'")
    print(f"Edit distance: {edit_distance(s1, s2)}")  # Expected: 3
    print(f"Edit distance (space optimized): {edit_distance_space_optimized(s1, s2)}")
    print(f"Edit distance (single array): {edit_distance_single_array(s1, s2)}")
    print()

    # Test case 5 - empty strings
    s1, s2 = "", "abc"
    print(f"s1 = '{s1}', s2 = '{s2}'")
    print(f"Edit distance: {edit_distance(s1, s2)}")  # Expected: 3
    print()

    # Test case 6
    s1, s2 = "abc", ""
    print(f"s1 = '{s1}', s2 = '{s2}'")
    print(f"Edit distance: {edit_distance(s1, s2)}")  # Expected: 3
    print()

    # Test case 7
    s1, s2 = "intention", "execution"
    print(f"s1 = '{s1}', s2 = '{s2}'")
    print(f"Edit distance: {edit_distance(s1, s2)}")  # Expected: 5
    print()

    # Verify all three implementations give the same result
    s1, s2 = "sunday", "saturday"
    print(f"s1 = '{s1}', s2 = '{s2}'")
    print(f"Edit distance: {edit_distance(s1, s2)}")
    print(f"Edit distance (space optimized): {edit_distance_space_optimized(s1, s2)}")
    print(f"Edit distance (single array): {edit_distance_single_array(s1, s2)}")
