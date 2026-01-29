def isSortedhelper(arr, n):
    # Base case
    if n == 0 or n == 1:
        return True
    
    # Check if current and previous elements are in order
    # and recursively check the rest of the array
    return arr[n - 1] >= arr[n - 2] and isSortedhelper(arr, n - 1)

def isSorted(arr):
    n = len(arr)
    return isSortedhelper(arr, n)

if __name__ == "__main__":
    arr1 = [10, 20, 30, 40, 50]
    print(f"Array {arr1} is sorted: {isSorted(arr1)}")
    
    arr2 = [10, 20, 30, 5, 6]
    print(f"Array {arr2} is sorted: {isSorted(arr2)}")
