def check_binary_palindrome(n: int) -> bool:
    """Check if binary representation of a number is palindrome."""
    rev = 0
    temp = n
    while temp > 0:
        rev = (rev << 1) | (temp & 1)
        temp >>= 1
    return rev == n


if __name__ == "__main__":
    print(check_binary_palindrome(5))
    print(check_binary_palindrome(9))
    print(check_binary_palindrome(7))
