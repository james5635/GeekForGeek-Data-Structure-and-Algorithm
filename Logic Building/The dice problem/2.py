""" Using Sum of Two Sides """
def opposite_face(n: int) -> int:
    """
    >>> opposite_face(1) 
    6
    >>> opposite_face(2) 
    5
    >>> opposite_face(3) 
    4
    """
    ans = 7 - n
    return ans
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)