## Test 0
from typing import Callable, Iterator, Tuple, Any

a = [[1, "apple"], [2, "orange"], [3, "cherry"]]
res: map[tuple[object, ...]] = map(tuple, a)
print(type(res))

## Test 1
x = (i for i in range(10))


def y(a):
    return a


k = (1, 2, 3)
l = (x for x in range(10))
n = [1, 2, 3]
m = [i for i in range(2)]
y(l for l in range(0, 20))

uu: dict[int,] = dict([1, 2, 3])
