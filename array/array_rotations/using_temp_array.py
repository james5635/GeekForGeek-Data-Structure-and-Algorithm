def rotate_arr(arr, d):
    n = len(arr)
    if n == 0:
        return
    # Handle case when d > n
    d %= n
    
    # Storing rotated version of array
    temp = [0] * n
    
    # Copy last d elements to the front of temp
    for i in range(d):
        temp[i] = arr[n - d + i]
    
    # Copy the first n - d elements to the back of temp
    for i in range(n - d):
        temp[i + d] = arr[i]
        
    # Copying the elements of temp in arr to get the final rotated array
    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2
    print(f"Original array: {arr}, d: {d}")
    rotate_arr(arr, d)
    print(f"Rotated array (using temp array): {arr}")
