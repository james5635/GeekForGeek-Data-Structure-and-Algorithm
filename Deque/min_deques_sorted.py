from collections import deque


def min_deques_to_make_array_sorted(arr):
    n = len(arr)
    if n == 0:
        return 0

    for k in range(1, n + 1):
        if can_split_into_k_deques(arr, k):
            return k

    return n


def can_split_into_k_deques(arr, k):
    if k == 1:
        return arr == sorted(arr)

    if k >= len(arr):
        return True

    deques = [deque() for _ in range(k)]

    def backtrack(idx):
        if idx == len(arr):
            return True

        num = arr[idx]

        for dq in deques:
            if len(dq) == 0:
                dq.append(num)
                if backtrack(idx + 1):
                    return True
                dq.pop()
            elif dq[-1] < num:
                dq.append(num)
                if backtrack(idx + 1):
                    return True
                dq.pop()

        return False

    return backtrack(0)


def main():
    # Test Case 1: [3, 6, 0, 9, 5, 4] -> 2
    print("Test Case 1: [3, 6, 0, 9, 5, 4]")
    arr1 = [3, 6, 0, 9, 5, 4]
    result1 = min_deques_to_make_array_sorted(arr1)
    print(f"Minimum deques required: {result1}")
    print(f"Expected: 2")
    print()

    # Test Case 2: Already sorted array -> 1
    print("Test Case 2: Already sorted [1, 2, 3, 4]")
    arr2 = [1, 2, 3, 4]
    result2 = min_deques_to_make_array_sorted(arr2)
    print(f"Minimum deques required: {result2}")
    print(f"Expected: 1")
    print()

    # Test Case 3: Reverse sorted -> N
    print("Test Case 3: Reverse sorted [4, 3, 2, 1]")
    arr3 = [4, 3, 2, 1]
    result3 = min_deques_to_make_array_sorted(arr3)
    print(f"Minimum deques required: {result3}")
    print(f"Expected: 4")
    print()

    # Test Case 4: Single element -> 1
    print("Test Case 4: Single element [5]")
    arr4 = [5]
    result4 = min_deques_to_make_array_sorted(arr4)
    print(f"Minimum deques required: {result4}")
    print(f"Expected: 1")
    print()

    # Test Case 5: Empty array -> 0
    print("Test Case 5: Empty array []")
    arr5 = []
    result5 = min_deques_to_make_array_sorted(arr5)
    print(f"Minimum deques required: {result5}")
    print(f"Expected: 0")
    print()

    # Test Case 6: [1, 0, 3, 2] -> 2
    print("Test Case 6: [1, 0, 3, 2]")
    arr6 = [1, 0, 3, 2]
    result6 = min_deques_to_make_array_sorted(arr6)
    print(f"Minimum deques required: {result6}")
    print()

    # Test Case 7: [5, 4, 3, 2, 1] -> 5
    print("Test Case 7: [5, 4, 3, 2, 1]")
    arr7 = [5, 4, 3, 2, 1]
    result7 = min_deques_to_make_array_sorted(arr7)
    print(f"Minimum deques required: {result7}")
    print(f"Expected: 5")


if __name__ == "__main__":
    main()
