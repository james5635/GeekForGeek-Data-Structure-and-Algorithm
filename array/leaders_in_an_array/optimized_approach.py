# Function to find the leaders in an array
def leaders(arr):
    result = []
    n = len(arr)
    
    # Start with the rightmost element
    max_right = arr[-1]
    
    # Rightmost element is always a leader
    result.append(max_right)
    
    # Traverse the array from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] >= max_right:
            max_right = arr[i]
            result.append(max_right)
    
    # Reverse the result list to maintain original order
    result.reverse()
    return result

if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    result = leaders(arr)
    print(" ".join(map(str, result)))
