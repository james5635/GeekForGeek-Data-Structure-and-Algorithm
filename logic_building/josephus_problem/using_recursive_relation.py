"""Expected Approach - 1: Using Recursive Relation - O(n) Time and O(n) Space"""


def josephus(n: int, k: int) -> int:
    """
    Solve the Josephus problem using recursive relation.
    
    There are n people standing in a circle, numbered from 1 to n. Starting
    from person 1, counting proceeds in clockwise direction. In each step,
    exactly k-1 people are skipped, and the k-th person is eliminated from
    the circle. The counting then resumes from the next person, and the
    process continues until only one person remains.
    
    The Josephus problem can be solved recursively using the relation:
    josephus(n, k) = (josephus(n-1, k) + k-1) % n + 1
    
    The key idea is after each elimination, the circle shrinks, but the
    pattern of safe positions stays the same it's just rotated. So if we
    know the safe position for n-1 people, we can shift it forward by k
    positions to get the safe position for n people. Repeat this
    shrinking-and-shifting idea until only 1 person remains, which is
    trivially safe.
    
    Working:
    - Base case: If there's only 1 person, return position 1.
    - Recursive call: Solve Josephus for n-1 people. This gives the safe
      position relative to the smaller circle.
    - Adjust for the shift: The eliminated person shifts positions by k.
      So the safe position in the original circle is
      (safe_from_smaller + k-1) % n + 1.
      +k-1: move forward by k steps (0-based counting).
      %n: wrap around the circle.
      +1: convert from 0-based to 1-based indexing.
    
    Time complexity: O(n)
    Auxiliary Space: O(n) - Function call stack space
    
    >>> josephus(5, 2)
    3
    >>> josephus(7, 3)
    4
    >>> josephus(1, 2)
    1
    """
    if n == 1:
        return 1
    else:
        # The position returned by josephus(n - 1, k) is adjusted because
        # the recursive call josephus(n - 1, k) considers the original
        # position k % n + 1 as position 1
        return (josephus(n - 1, k) + k - 1) % n + 1


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
