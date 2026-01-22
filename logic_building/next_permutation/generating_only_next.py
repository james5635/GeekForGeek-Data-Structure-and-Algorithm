"""Expected Approach - Generating Only Next - O(n) Time and O(1) Space"""


def next_permutation(arr: list[int]) -> None:
    """
    Find the next lexicographically greater permutation.
    
    Observations of Next permutation:
    1. To get the next permutation we change the number in a position which is
       as right as possible.
    2. The first number to be moved is the rightmost number smaller than its next.
    3. The number to come in-place is the rightmost greater number on right
       side of the pivot.
    
    Each permutation (except the very first) has an increasing suffix. Now if
    we change the pattern from the pivot point (where the increasing suffix
    breaks) to its next possible lexicographic representation we will get the
    next greater permutation.
    
    Step-By-Step Approach:
    - Iterate over the given array from end and find the first index (pivot)
      which doesn't follow property of non-increasing suffix,
      (i.e, arr[i] < arr[i + 1]).
    - If pivot index does not exist, then the given sequence in the array is
      the largest as possible. So, reverse the complete array.
    - Otherwise, Iterate the array from the end and find for the successor
      (rightmost greater element) of pivot in suffix.
    - Swap the pivot and successor
    - Minimize the suffix part by reversing the array from pivot + 1 till n.
    
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
    n = len(arr)

    # Find the pivot index
    pivot = -1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            pivot = i
            break

    # If pivot point does not exist, reverse the whole array
    if pivot == -1:
        arr.reverse()
        return

    # Find the element from the right that is greater than pivot
    for i in range(n - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break

    # Reverse the elements from pivot + 1 to the end in place
    left, right = pivot + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
