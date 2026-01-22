"""Expected Approach - 2: Iterative Mathematical Approach - O(n) Time and O(1) Space"""


def josephus(n: int, k: int) -> int:
    """
    Solve the Josephus problem using iterative mathematical approach.
    
    There are n people standing in a circle, numbered from 1 to n. Starting
    from person 1, counting proceeds in clockwise direction. In each step,
    exactly k-1 people are skipped, and the k-th person is eliminated from
    the circle. The counting then resumes from the next person, and the
    process continues until only one person remains.
    
    We can solve this iteratively by building the solution from 1 person up
    to n.
    
    - For 1 person, the safe position is obviously 1.
    - When we add a new person, the safe position shifts by k (because every
      k-th person is eliminated), wrapping around the current circle size.
    - Repeating this update until n people gives the final survivor.
    
    Time complexity: O(n)
    Auxiliary Space: O(1)
    
    >>> josephus(5, 2)
    3
    >>> josephus(7, 3)
    4
    >>> josephus(1, 2)
    1
    """
    # Initialize variables i and ans with 1 and 0 respectively.
    i = 1
    ans = 0

    # Run a while loop till i <= n
    while i <= n:
        # Update the Value of ans and Increment i by 1
        ans = (ans + k) % i
        i += 1

    # Return required answer
    return ans + 1


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
