"""Find if two rectangles overlap."""


def rectangles_overlap(
    l1x: float,
    l1y: float,
    r1x: float,
    r1y: float,
    l2x: float,
    l2y: float,
    r2x: float,
    r2y: float,
) -> bool:
    """Check if two axis-aligned rectangles overlap.

    Args:
        l1x, l1y: Top-left corner of rectangle 1.
        r1x, r1y: Bottom-right corner of rectangle 1.
        l2x, l2y: Top-left corner of rectangle 2.
        r2x, r2y: Bottom-right corner of rectangle 2.

    Returns:
        True if rectangles overlap, False otherwise.
    """
    if l1x > r2x or l2x > r1x:
        return False
    if l1y < r2y or l2y < r1y:
        return False
    return True


if __name__ == "__main__":
    print(f"Overlap: {rectangles_overlap(0, 10, 10, 0, 5, 5, 15, -5)}")
    print(f"Overlap: {rectangles_overlap(0, 10, 2, 5, 3, 4, 5, 0)}")
