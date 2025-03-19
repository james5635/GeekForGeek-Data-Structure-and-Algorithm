from typing import Callable, Iterator, Tuple, Any
a = [[1, "apple"], [2, "orange"], [3, "cherry"]]
res: map[tuple[object, ...]] = map(tuple, a)
print(type(res))