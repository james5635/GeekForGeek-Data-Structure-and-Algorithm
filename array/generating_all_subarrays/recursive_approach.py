# Recursive function to print all possible subarrays for given array
def printSubArrays(arr, start, end):
    # Stop if we have reached the end of the array
    if end == len(arr):
        return
    # Increment the end point and start from 0
    elif start > end:
        return printSubArrays(arr, 0, end + 1)
    # Print the subarray and increment the starting point
    else:
        print(arr[start:end + 1])
        return printSubArrays(arr, start + 1, end)

if __name__ == "__main__":
    # Driver code
    arr = [1, 2, 3]
    print("All Non-empty Subarrays (Recursive):")
    printSubArrays(arr, 0, 0)
