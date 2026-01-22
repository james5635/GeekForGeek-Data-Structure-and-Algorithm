"""Better Approach - By using Dynamic Programming"""


def find_catalan(n: int) -> int:
    """
    Find the nth Catalan number using dynamic programming.
    
    We can observe that the recursive implementation does a lot of repeated work.
    Since there are overlapping subproblems, we can use dynamic programming for this.
    
    Step-by-step approach:
    - Create an array catalan[] for storing ith Catalan number.
    - Initialize, catalan[0] and catalan[1] = 1
    - Loop through i = 2 to the given Catalan number n.
      - Loop through j = 0 to j < i and Keep adding value of
        catalan[j] * catalan[i - j - 1] into catalan[i].
    - Finally, return catalan[n]
    
    >>> find_catalan(0)
    1
    >>> find_catalan(1)
    1
    >>> find_catalan(2)
    2
    >>> find_catalan(3)
    5
    >>> find_catalan(4)
    14
    >>> find_catalan(5)
    42
    >>> find_catalan(6)
    132
    """
    # Table to store results of subproblems
    catalan = [0] * (n + 1)

    # Initialize first two values in the table
    catalan[0] = catalan[1] = 1

    # Fill entries in catalan[] using the recursive formula
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]

    # Return the last entry
    return catalan[n]


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
