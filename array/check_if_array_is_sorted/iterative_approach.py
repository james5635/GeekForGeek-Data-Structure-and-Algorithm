def isSorted(arr):
    n = len(arr)
    # Iterate over the array and check if
    # every element is greater than or
    # equal to previous element.
    for i in range(1, n):
        if arr[i-1] > arr[i]:
            return False
    return True

if __name__ == "__main__":
    arr1 = [10, 20, 30, 40, 50]
    print(f"Array {arr1} is sorted: {isSorted(arr1)}")
    
    arr2 = [10, 20, 30, 5, 6]
    print(f"Array {arr2} is sorted: {isSorted(arr2)}")
