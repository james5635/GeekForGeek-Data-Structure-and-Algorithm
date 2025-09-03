""" Naive Approach """
def power(x: int, y: int) -> int:
    if y ==0 :
        return 1
    if y % 2 ==0:
        return power(x, y // 2) * power(x, y //2)
    return x * power(x, y // 2) * power(x, y // 2)
def order(n: int) -> int:
    t = 0
    while n:
        t += 1
        n //= 10
    return t
def armstrong(n: int) -> bool:
    """
    >>> armstrong(153)
    True
    """
    order_ = order(n)
    temp = n
    sum = 0
    while temp:
        res = temp % 10
        sum += power(res, order_)
        temp //= 10
    return sum == n
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)
