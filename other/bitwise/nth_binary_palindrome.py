def nth_binary_palindrome(n: int) -> str:
    """Find n-th number whose binary representation is palindrome."""
    count = 0
    num = 0
    while count < n:
        num += 1
        if check_binary_palindrome(num):
            count += 1
    return bin(num)[2:]


def check_binary_palindrome(n: int) -> bool:
    """Check if binary representation is palindrome."""
    rev = 0
    temp = n
    while temp > 0:
        rev = (rev << 1) | (temp & 1)
        temp >>= 1
    return rev == n


if __name__ == "__main__":
    print(nth_binary_palindrome(1))
    print(nth_binary_palindrome(5))
    print(nth_binary_palindrome(10))
