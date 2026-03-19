def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result


if __name__ == "__main__":
    arr1 = [4, 5, 2, 25]
    print("Array:", arr1)
    print("Next greater element:", next_greater_element(arr1))

    arr2 = [13, 7, 6, 12]
    print("\nArray:", arr2)
    print("Next greater element:", next_greater_element(arr2))

    arr3 = [1, 3, 2, 4]
    print("\nArray:", arr3)
    print("Next greater element:", next_greater_element(arr3))
