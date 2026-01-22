"""Naive Approach - 1: Recursively Removing Elements - O(n^2) Time and O(n) Space"""


def josephus_rec(person: list[int], k: int, index: int) -> int:
    """
    Helper function to recursively solve Josephus problem.
    
    >>> josephus_rec([1, 2, 3, 4, 5], 2, 0)
    3
    """
    # Base case, when only one person is left
    if len(person) == 1:
        return person[0]

    # Find the index of first person which will die
    index = (index + k) % len(person)

    # Remove the first person which is going to be killed
    person.pop(index)

    # Recursive call for n-1 persons
    return josephus_rec(person, k, index)


def josephus(n: int, k: int) -> int:
    """
    Solve the Josephus problem using recursive removal of elements.
    
    There are n people standing in a circle, numbered from 1 to n. Starting
    from person 1, counting proceeds in clockwise direction. In each step,
    exactly k-1 people are skipped, and the k-th person is eliminated from
    the circle. The counting then resumes from the next person, and the
    process continues until only one person remains.
    
    We can store people in an array from 1 to n. Since counting is 0-based
    in the code, we use k-1 instead of k. Starting at index 0, in each step
    we remove the person at position: (index + (k-1)) % current size.
    
    After removing, the recursive call continues from this new index with
    the reduced array. This process repeats until only one person remains,
    who is the survivor.
    
    Time complexity: O(n^2)
    Auxiliary Space: O(n)
    
    >>> josephus(5, 2)
    3
    >>> josephus(7, 3)
    4
    >>> josephus(1, 2)
    1
    """
    # The index where the person which will die
    index = 0

    person = []

    # Fill the person vector
    for i in range(1, n + 1):
        person.append(i)

    return josephus_rec(person, k, index)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
