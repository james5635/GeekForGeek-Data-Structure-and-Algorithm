""" Iterative Checking """

def closest_number(n:int,m:int) -> int:
    """
    <<< closest_number(10, 3)
    9
    <<< closest_number(10, 5)
    10
    <<< closest_number(15674.246)
    15675
    """
    closest = 0
    min_diff = float('inf')

    for i in range(n-abs(m), n+abs(m)+1):
        if i % m == 0:
            diff = abs(n - i)
            if diff < min_diff or (diff == min_diff and abs(i) >  abs(closest)):
                closest = i
                min_diff = diff
    return closest
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)