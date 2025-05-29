""" By finding Quotient """

def closest_number(n:int, m:int ) -> int:
    """
    <<< closest_number(10, 3)
    10
    <<< closest_number(10222, 5)
    10220
    <<< closest_number(152123123, 3213)
    152123121
    <<< closest_number(22234, 342)
    22236
    """
    # Find the quotient
    # q = n // m
    q = int (n / m)

    # First possible closest number
    n1 = m * q

    # Second possible closest number
    if n * m > 0:
        n2 = m * (q + 1)
    else:
        n2 = m * (q - 1)

    if abs(n - n1) < abs(n - n2):
        return n1
    return n2
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)