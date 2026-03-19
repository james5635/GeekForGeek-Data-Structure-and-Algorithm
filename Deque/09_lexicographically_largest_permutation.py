from collections import deque


def largest_permutation(arr):
    dq = deque()
    for x in arr:
        if not dq or x >= dq[0]:
            dq.appendleft(x)
        else:
            dq.append(x)
    return list(dq)


if __name__ == "__main__":
    assert largest_permutation([3, 1, 2, 4]) == [4, 3, 1, 2]
    assert largest_permutation([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert largest_permutation([4, 3, 2, 1]) == [4, 3, 2, 1]
    assert largest_permutation([1]) == [1]
    assert largest_permutation([2, 1]) == [2, 1]
    assert largest_permutation([1, 2]) == [2, 1]
    assert largest_permutation([5, 3, 1, 4, 2]) == [5, 3, 1, 4, 2]
    assert largest_permutation([3, 3, 1]) == [3, 3, 1]
    assert largest_permutation([2, 3, 1]) == [3, 2, 1]

    print("All tests passed")
