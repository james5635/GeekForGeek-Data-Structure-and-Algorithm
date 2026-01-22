"""Naive Approach - 2: Using Iterative Simulation - O(n^2) Time and O(n) Space"""


def josephus(n: int, k: int) -> int:
    """
    Solve the Josephus problem using iterative simulation.
    
    There are n people standing in a circle, numbered from 1 to n. Starting
    from person 1, counting proceeds in clockwise direction. In each step,
    exactly k-1 people are skipped, and the k-th person is eliminated from
    the circle. The counting then resumes from the next person, and the
    process continues until only one person remains.
    
    The idea is to use an array to mark alive people. Initially, all people
    are alive. Starting from the first person, we count k alive persons in
    the circle, skipping those already eliminated. When we reach the k-th
    alive person, we mark them as dead.
    
    After each elimination, counting resumes from the next alive person. We
    continue this process iteratively, handling the circular nature by
    wrapping around the array indices, until only one person remains alive.
    
    Time complexity: O(n^2)
    Auxiliary Space: O(n)
    
    >>> josephus(5, 2)
    3
    >>> josephus(7, 3)
    4
    >>> josephus(1, 2)
    1
    """
    k -= 1
    arr = [0] * n

    # Makes all the 'n' people alive by assigning them value = 1
    for i in range(n):
        arr[i] = 1

    cnt = 0
    cut = 0
    # Cut = 0 gives the sword to 1st person.
    num = 1

    # Loop continues till n-1 person dies.
    while cnt < (n - 1):
        # Checks next (kth) alive persons.
        while num <= k:
            cut += 1

            # Checks and resolves overflow of Index.
            cut = cut % n
            if arr[cut] == 1:
                # Updates the number of persons alive.
                num += 1

        # Refreshes value to 1 for next use.
        num = 1

        # Kills the person at position of 'cut'
        arr[cut] = 0

        # Updates the no. of killed persons.
        cnt += 1
        cut += 1

        # Checks and resolves overflow of Index.
        cut = cut % n

        # Checks the next alive person the sword is to be given.
        while arr[cut] == 0:
            cut += 1

            # Checks and resolves overflow of Index.
            cut = cut % n

    # Output is the position of the last man alive (Index + 1)
    return cut + 1


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
