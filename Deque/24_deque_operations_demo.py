from collections import deque


def demo_append_operations():
    dq = deque()
    dq.append(1)
    dq.append(2)
    dq.append(3)
    dq.appendleft(0)
    dq.appendleft(-1)
    assert list(dq) == [-1, 0, 1, 2, 3]
    return dq


def demo_pop_operations():
    dq = deque([1, 2, 3, 4, 5])
    right = dq.pop()
    left = dq.popleft()
    assert right == 5
    assert left == 1
    assert list(dq) == [2, 3, 4]
    return dq


def demo_rotate():
    dq = deque([1, 2, 3, 4, 5])
    dq.rotate(2)
    assert list(dq) == [4, 5, 1, 2, 3]
    dq.rotate(-3)
    assert list(dq) == [2, 3, 4, 5, 1]
    return dq


def demo_maxlen():
    dq = deque(maxlen=3)
    dq.append(1)
    dq.append(2)
    dq.append(3)
    assert list(dq) == [1, 2, 3]
    dq.append(4)
    assert list(dq) == [2, 3, 4]
    dq.appendleft(0)
    assert list(dq) == [0, 2, 3]
    return dq


def demo_extend():
    dq = deque([1, 2])
    dq.extend([3, 4, 5])
    assert list(dq) == [1, 2, 3, 4, 5]
    dq.extendleft([0, -1])
    assert list(dq) == [-1, 0, 1, 2, 3, 4, 5]
    return dq


def demo_clear_and_len():
    dq = deque([1, 2, 3, 4, 5])
    assert len(dq) == 5
    assert 3 in dq
    dq.clear()
    assert len(dq) == 0
    assert list(dq) == []
    return dq


if __name__ == "__main__":
    demo_append_operations()
    demo_pop_operations()
    demo_rotate()
    demo_maxlen()
    demo_extend()
    demo_clear_and_len()
    print("All tests passed!")
