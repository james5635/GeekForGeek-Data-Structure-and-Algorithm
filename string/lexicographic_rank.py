"""
Lexicographic Rank of a String

Given a string, find its rank among all its permutations when sorted lexicographically.
Note: The characters in string are all unique.

Examples:
- Input: "acb" -> Output: 2
- Input: "string" -> Output: 598

Time Complexity: O(n^2) for the optimized approach
Space Complexity: O(1)
"""


def fact(n):
    """Calculate factorial of n"""
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def findSmallerInRight(s, low):
    """
    Count smaller characters on right of s[low]
    """
    countRight = 0
    for i in range(low + 1, len(s)):
        if s[i] < s[low]:
            countRight += 1
    return countRight


def findRank(s):
    """
    Find lexicographic rank of a string
    Uses O(n^2) approach with repeated factorial computation
    """
    n = len(s)
    mul = fact(n)
    rank = 1

    for i in range(n):
        mul //= n - i

        # Count number of chars smaller than s[i]
        # from s[i+1] to s[len-1]
        countRight = findSmallerInRight(s, i)

        rank += countRight * mul

    return rank


def findRankOptimized(s):
    """
    Find lexicographic rank using frequency array - O(n) time
    """
    n = len(s)
    mul = fact(n)
    rank = 1

    # Using a vector of size 26 for lowercase letters
    count = [0] * 26

    # Populate the count array for each character in string
    for i in range(n):
        count[ord(s[i]) - ord("a")] += 1

    # Convert count to cumulative sum
    for i in range(1, 26):
        count[i] += count[i - 1]

    for i in range(n):
        mul //= n - i

        # Get index of current character in count array
        charIndex = ord(s[i]) - ord("a")

        # Add count of characters smaller than current character
        if charIndex > 0:
            rank += count[charIndex - 1] * mul

        # Update count array
        for j in range(charIndex, 26):
            count[j] -= 1

    return rank


# Test the functions
if __name__ == "__main__":
    test_cases = ["acb", "string", "cba"]

    print("Lexicographic Rank of Strings")
    print("=" * 40)

    for s in test_cases:
        rank = findRank(s)
        rank_opt = findRankOptimized(s)
        print(f"String: '{s}'")
        print(f"  Rank (O(n^2) approach): {rank}")
        print(f"  Rank (O(n) approach):   {rank_opt}")
        print()

    # Explanation for "acb"
    print("Explanation for 'acb':")
    print("All permutations in lexicographic order:")
    print("1. abc")
    print("2. acb <- This is our string")
    print("3. bac")
    print("4. bca")
    print("5. cab")
    print("6. cba")
    print("\nSo rank of 'acb' is 2")
