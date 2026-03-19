def max_of_mins_every_window(arr):
    n = len(arr)

    prev_smaller = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            prev_smaller[i] = stack[-1]
        stack.append(i)

    next_smaller = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            next_smaller[i] = stack[-1]
        stack.append(i)

    result = [float("-inf")] * (n + 1)
    for i in range(n):
        length = next_smaller[i] - prev_smaller[i] - 1
        result[length] = max(result[length], arr[i])

    for i in range(n - 1, 0, -1):
        result[i] = max(result[i], result[i + 1])

    return result[1 : n + 1]


if __name__ == "__main__":
    arr1 = [10, 20, 30, 50, 10, 70, 30]
    print("Array:", arr1)
    print("Max of mins:", max_of_mins_every_window(arr1))

    arr2 = [10, 20, 30]
    print("\nArray:", arr2)
    print("Max of mins:", max_of_mins_every_window(arr2))

    arr3 = [6, 5, 4, 3, 2, 1]
    print("\nArray:", arr3)
    print("Max of mins:", max_of_mins_every_window(arr3))
