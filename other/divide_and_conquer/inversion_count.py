def count_inversions(arr: list[int]) -> int:
    """
    Count the number of inversions in an array using modified merge sort.

    An inversion is a pair (i, j) such that i < j and arr[i] > arr[j].

    Args:
        arr: List of integers

    Returns:
        Number of inversions in the array
    """
    if len(arr) <= 1:
        return 0

    return _merge_sort_count(arr, 0, len(arr) - 1)


def _merge_sort_count(arr: list[int], left: int, right: int) -> int:
    if left >= right:
        return 0

    mid = (left + right) // 2
    count = _merge_sort_count(arr, left, mid)
    count += _merge_sort_count(arr, mid + 1, right)
    count += _merge_count(arr, left, mid, right)

    return count


def _merge_count(arr: list[int], left: int, mid: int, right: int) -> int:
    temp = []
    i = left
    j = mid + 1
    count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            count += mid - i + 1
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for k in range(len(temp)):
        arr[left + k] = temp[k]

    return count


if __name__ == "__main__":
    arr1 = [8, 4, 2, 1]
    print(count_inversions(arr1))

    arr2 = [3, 1, 2]
    print(count_inversions(arr2))
