"""
Print All Combinations of Balanced Parentheses

Given a number n (where n represents pairs of parentheses),
print all combinations of balanced parentheses of length 2n.

A sequence is balanced if every opening bracket '(' has a corresponding
closing bracket ')' in the correct order.

Approach: Backtracking
- Only add '(' if count of open brackets < n
- Only add ')' if count of close brackets < count of open brackets
- When current string length = 2n, we have a valid combination

Examples:
    Input: n = 2 (1 pair)
    Output: ["()"]

    Input: n = 4 (2 pairs)
    Output: ["(())", "()()"]

    Input: n = 6 (3 pairs)
    Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
"""


def validParentheses(n: int, openCount: int, curr: str, res: list) -> None:
    """
    Recursive function to generate valid parentheses sequences.

    Args:
        n: Total pairs of parentheses needed
        openCount: Count of opening brackets used so far
        curr: Current string being built
        res: Result list to store valid sequences
    """
    # Base case: If current sequence has reached length 2n
    if len(curr) == 2 * n:
        res.append(curr)
        return

    # Add opening parenthesis if we haven't used all n opening parentheses
    if openCount < n:
        validParentheses(n, openCount + 1, curr + "(", res)

    # Add closing parenthesis if count of closing < count of opening
    # This ensures each closing has a matching opening before it
    if len(curr) - openCount < openCount:
        validParentheses(n, openCount, curr + ")", res)


def generateParentheses(n: int) -> list:
    """
    Generate all valid combinations of n pairs of parentheses.

    Args:
        n: Number of pairs (note: input is total length, so we use n//2 pairs)

    Returns:
        List of all valid parentheses combinations

    Time Complexity: O(C_n * n), where C_n is the nth Catalan number
    Space Complexity: O(n) for recursion stack
    """
    res = []
    # n//2 gives us the number of pairs (since total length is 2n)
    pairs = n // 2 if n % 2 == 0 else n
    validParentheses(pairs, 0, "", res)
    return res


def generateParenthesesPairs(pairs: int) -> list:
    """
    Generate all valid combinations given number of pairs directly.

    Args:
        pairs: Number of pairs of parentheses

    Returns:
        List of all valid combinations
    """
    res = []
    validParentheses(pairs, 0, "", res)
    return res


def isValidParentheses(s: str) -> bool:
    """
    Helper function to check if a parentheses sequence is valid.

    Args:
        s: String of parentheses

    Returns:
        True if valid, False otherwise
    """
    count = 0
    for char in s:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
            if count < 0:
                return False
    return count == 0


def main():
    """Test the balanced parentheses functions."""
    print("=" * 60)
    print("Print All Combinations of Balanced Parentheses")
    print("=" * 60)

    test_cases = [2, 4, 6, 8]

    for n in test_cases:
        pairs = n // 2
        print(f"\nn = {n} ({pairs} pair{'s' if pairs > 1 else ''})")
        print("-" * 40)

        result = generateParentheses(n)
        print(f"Total combinations: {len(result)}")
        print("Combinations:")
        for seq in result:
            # Verify validity
            valid = "✓" if isValidParentheses(seq) else "✗"
            print(f"  {valid} '{seq}'")

    print("\n" + "=" * 60)
    print("Complexity Analysis:")
    print("=" * 60)
    print("Time Complexity: O(C_n * n)")
    print("  - C_n is the nth Catalan number: (2n)! / ((n+1)! * n!)")
    print("  - Number of valid combinations follows Catalan sequence:")
    print("    n=1: 1, n=2: 2, n=3: 5, n=4: 14, n=5: 42, ...")
    print("Space Complexity: O(n)")
    print("  - Recursion stack depth")
    print("  - Temporary string storage")

    print("\n" + "=" * 60)
    print("Catalan Numbers (valid combinations count):")
    print("=" * 60)
    for pairs in range(1, 6):
        result = generateParenthesesPairs(pairs)
        print(f"  {pairs} pair{'s' if pairs > 1 else ''}: {len(result)} combinations")


if __name__ == "__main__":
    main()
