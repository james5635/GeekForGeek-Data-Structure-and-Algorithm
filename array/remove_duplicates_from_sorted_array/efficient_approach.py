def remove_duplicates(arr):
    n = len(arr)
    if n <= 1:
        return n

    # Start from the second element
    idx = 1
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[idx] = arr[i]
            idx += 1
    return idx

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    print(f"Original array: {arr}")
    new_size = remove_duplicates(arr)
    print(f"Modified array: {arr[:new_size]}")
    print(f"New size: {new_size}")
