"""condition method"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def is_overlap(l1, r1, l2, r2):
    """
    test to see if two of the rectangles overlap

    >>> is_overlap(Point(0, 10),Point(10, 0),Point(5, 5),Point(15, 0))
    True
    """
    if l1.x > r2.x or l2.x > r1.x:
        return False
    if r1.y > l2.y or r2.y > l1.y:
        return False
    return True


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
