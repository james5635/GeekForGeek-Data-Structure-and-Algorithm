"""Approach: Using Mathematical Formula - O(1) Time and O(1) Space"""


import math


def min_rats(n: int) -> int:
    """
    Find the minimum number of rats required to identify the poisoned bottle.
    
    Given N number of bottles in which one bottle is poisoned, find out the
    minimum number of rats required to identify the poisoned bottle. A rat can
    drink any number of bottles at a time and if any of the taken bottles is
    poisonous, then the rat dies and cannot drink anymore.
    
    Approach:
    The solution uses binary representation to identify the poisoned bottle.
    Each rat represents a bit position in the binary representation of bottle
    numbers. By having rats drink from bottles based on their binary
    representation, we can uniquely identify the poisoned bottle.
    
    Examples:
    - For 2 bottles: 1 rat is enough (2^1 = 2)
    - For 3 bottles: 2 rats are needed (2^2 = 4 >= 3)
    - For 4 bottles: 2 rats are needed (2^2 = 4 >= 4)
    - For 100 bottles: 7 rats are needed (2^7 = 128 >= 100)
    - For 1000 bottles: 10 rats are needed (2^10 = 1024 >= 1000)
    
    The minimum number of rats required is ceil(log2(n)), because:
    - With k rats, we can identify up to 2^k bottles
    - We need the smallest k such that 2^k >= n
    - This is equivalent to k >= log2(n)
    - Therefore, k = ceil(log2(n))
    
    Time Complexity: O(1)
    Auxiliary Space: O(1)
    
    >>> min_rats(4)
    2
    >>> min_rats(100)
    7
    >>> min_rats(1000)
    10
    >>> min_rats(2)
    1
    >>> min_rats(1)
    0
    >>> min_rats(1025)
    11
    """
    if n <= 1:
        # If there's only 1 bottle, no rats needed (it must be the poisoned one)
        # If n <= 0, invalid input, return 0
        return 0
    
    return math.ceil(math.log2(n))


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
