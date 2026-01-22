"""Approach: By Using Binary Representation of Numbers from 0 to 2^n - 1"""


def all_possible_strings(s: str) -> list[str]:
    """
    Find the power set of a string using binary representation.
    
    For a given set S, the power set can be found by generating all binary
    numbers between 0 and 2^n - 1, where n is the size of the set.
    
    Example: Set = [a, b, c]
    power_set_size = pow(2, 3) = 8
    Run for binary counter = 000 to 111. We consider a when the last bit is
    set and do not consider if the last bit is not set. We do the same thing
    for b and second bit, and for c and first bit.
    
    Value of Counter | Subset
    000              | Empty set
    001              | a
    010              | b
    011              | ab
    100              | c
    101              | ac
    110              | bc
    111              | abc
    
    Detailed Steps:
    - Get the size of power set: power_set_size = pow(2, set_size)
    - Loop for counter from 0 to power_set_size
      - Loop for i = 0 to set_size
        - If ith bit in counter is set, Print ith element from set for this subset
      - Add the subset to the result
    
    >>> result = all_possible_strings("ab")
    >>> sorted(result)
    ['', 'a', 'ab', 'b']
    >>> result = all_possible_strings("abc")
    >>> sorted(result)
    ['', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
    >>> result = all_possible_strings("a")
    >>> sorted(result)
    ['', 'a']
    """
    n = len(s)
    result = []

    # Iterate through all subsets (represented by 0 to 2^n - 1)
    for i in range(1 << n):
        subset = ""
        for j in range(n):
            # Check if the j-th bit is set in i
            if i & (1 << j):
                subset += s[j]

        # Add the subset to the result
        result.append(subset)

    return result


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
