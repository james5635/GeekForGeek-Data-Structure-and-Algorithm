"""
Minimum Bracket Reversals to Make Expression Balanced

Given an expression with only '}' and '{'. The expression may not be balanced.
Find minimum number of bracket reversals to make the expression balanced.

Examples:
- s = "}{{}}{{{" -> Output: 3
  Explanation: Reverse 3 brackets to make "{{{}}}{}}"

- s = "{{" -> Output: 1

- s = "{{}{{{}{{}}{{" -> Output: -1
  Explanation: Odd length, cannot be balanced

Time Complexity: O(n)
Space Complexity: O(1) for optimized approach, O(n) for stack approach
"""


def countMinReversalsStack(expr):
    """
    Stack-based approach - O(n) time and O(n) space
    """
    length = len(expr)

    # Length of expression must be even to make it balanced
    if length % 2:
        return -1

    stack = []
    for char in expr:
        if char == "}" and stack:
            if stack[-1] == "{":
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)

    # Length of the reduced expression
    red_len = len(stack)

    # Count opening brackets at the end of stack
    n = 0
    while stack and stack[-1] == "{":
        stack.pop()
        n += 1

    # Return ceil(m/2) + ceil(n/2) which is equal to
    # (m+n)/2 + n%2 when m+n is even
    return red_len // 2 + n % 2


def countMinReversals(expr):
    """
    Optimized two-pointer approach - O(n) time and O(1) space
    """
    length = len(expr)

    # Expressions of odd lengths cannot be balanced
    if length % 2 != 0:
        return -1

    left_brace = 0
    right_brace = 0

    for char in expr:
        # If we find a left bracket then we
        # simply increment the left bracket
        if char == "{":
            left_brace += 1
        # Else if left bracket is 0 then we find
        # unbalanced right bracket and increment
        # right bracket or if the expression
        # is balanced then we decrement left
        else:
            if left_brace == 0:
                right_brace += 1
            else:
                left_brace -= 1

    # Calculate minimum reversals
    # ceil(left/2) + ceil(right/2)
    ans = (left_brace + 1) // 2 + (right_brace + 1) // 2
    return ans


# Test the functions
if __name__ == "__main__":
    test_cases = [
        "}{{}}{{{",
        "{{",
        "{{}{{{}{{}}{{",
        "}{{}}{{{{",
        "{{{{{{",
        "}}}}}}",
        "{}{}{}{}",
    ]

    print("Minimum Bracket Reversals")
    print("=" * 40)

    for expr in test_cases:
        result_stack = countMinReversalsStack(expr)
        result_opt = countMinReversals(expr)

        print(f"Expression: '{expr}'")
        print(f"  Length: {len(expr)}")
        print(f"  Stack approach: {result_stack}")
        print(f"  Optimized approach: {result_opt}")

        if result_opt == -1:
            print("  -> Cannot be balanced (odd length)")
        elif result_opt == 0:
            print("  -> Already balanced")
        else:
            print(f"  -> Need {result_opt} reversal(s)")
        print()
