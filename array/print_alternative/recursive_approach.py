# Recursive Python Program to print alternate elements of the array

# Recursive function to store all alternate elements
def getAlternatesRec(arr, idx, res):
    if idx < len(arr):
        res.append(arr[idx])
        getAlternatesRec(arr, idx + 2, res)


def getAlternates(arr):
    res = []
    getAlternatesRec(arr, 0, res)
    return res


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    res = getAlternates(arr)
    print(" ".join(map(str, res)))
