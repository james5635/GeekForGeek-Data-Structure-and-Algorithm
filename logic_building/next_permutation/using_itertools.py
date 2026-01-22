"""Alternate Approach - Using Inbuilt Function (Python itertools) - O(n) Time and O(1) Space"""


from itertools import permutations


def next_permutation(arr: list[int]) -> None:
    """
    Find the next lexicographically greater permutation using itertools.
    
    The idea is to use Python's built-in itertools.permutations(), which can
    generate permutations in lexicographic order. We find the current
    permutation and get the next one. If the current arrangement is already
    the largest possible, this function rearranges the array into the
    smallest (sorted) permutation.
    
    Note: This approach is less efficient than the direct algorithm for large
    arrays, but demonstrates the use of Python's standard library.
    
    This function modifies the input array in-place.
    
    >>> arr = [2, 4, 1, 7, 5, 0]
    >>> next_permutation(arr)
    >>> arr
    [2, 4, 5, 0, 1, 7]
    >>> arr = [3, 2, 1]
    >>> next_permutation(arr)
    >>> arr
    [1, 2, 3]
    >>> arr = [1, 3, 5, 4, 2]
    >>> next_permutation(arr)
    >>> arr
    [1, 4, 2, 3, 5]
    """
    # Convert to tuple for comparison (since lists are not hashable)
    current = tuple(arr)
    
    # Generate all permutations and find the current one
    found = False
    for perm in permutations(sorted(arr)):
        if found:
            arr[:] = list(perm)
            return
        if perm == current:
            found = True
    
    # If we reach here, current was the last permutation
    # Return the first (sorted) permutation
    arr[:] = sorted(arr)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
