def next_greater_frequency_element(arr):
    n = len(arr)
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1

    result = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and freq[arr[stack[-1]]] <= freq[arr[i]]:
            stack.pop()
        if stack:
            result[i] = arr[stack[-1]]
        stack.append(i)
    return result


if __name__ == "__main__":
    arr1 = [1, 1, 2, 3, 4, 2, 1]
    print("Array:", arr1)
    print("Next greater frequency:", next_greater_frequency_element(arr1))

    arr2 = [1, 2, 3, 4, 3]
    print("\nArray:", arr2)
    print("Next greater frequency:", next_greater_frequency_element(arr2))

    arr3 = [3, 4, 2, 7, 5, 8, 10, 6, 3, 2]
    print("\nArray:", arr3)
    print("Next greater frequency:", next_greater_frequency_element(arr3))
