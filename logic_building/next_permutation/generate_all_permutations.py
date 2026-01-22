"""Naive Approach - Generate All Permutations - O(n! * n) Time and O(n! * n) Space"""


def generate_permutations(res: list[list[int]], arr: list[int], idx: int) -> None:
    """
    Helper function to generate all possible permutations.
    
    >>> res = []
    >>> arr = [1, 2]
    >>> generate_permutations(res, arr, 0)
    >>> sorted(res)
    [[1, 2], [2, 1]]
    """
    # Base case: if idx reaches the end of array
    if idx == len(arr) - 1:
        res.append(arr[:])
        return

    # Generate all permutations by swapping
    for i in range(idx, len(arr)):
        arr[idx], arr[i] = arr[i], arr[idx]

        # Recur for the next index
        generate_permutations(res, arr, idx + 1)

        # Backtrack to restore original array
        arr[idx], arr[i] = arr[i], arr[idx]


def next_permutation(arr: list[int]) -> None:
    """
    Find the next lexicographically greater permutation.
    
    The idea is that we would first generate all possible permutations of a
    given array and sort them. Once sorted, we locate the current permutation
    within this list. The next permutation is simply the next arrangement in
    the sorted order. If the current arrangement is the last in the list
    then display the first permutation (smallest permutation).
    
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
    res = []

    # Generate all permutations
    generate_permutations(res, arr, 0)

    # Sort all permutations lexicographically
    res.sort()

    # Find the current permutation index
    for i in range(len(res)):
        # If current permutation matches input
        if res[i] == arr:
            # If it's not the last permutation
            if i < len(res) - 1:
                arr[:] = res[i + 1]
            # If it's the last permutation
            else:
                arr[:] = res[0]
            break


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
