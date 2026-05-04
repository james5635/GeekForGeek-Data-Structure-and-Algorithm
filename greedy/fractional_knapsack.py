# Fractional Knapsack - GeeksforGeeks
# Source: https://www.geeksforgeeks.org/dsa/fractional-knapsack-problem/


def fractionalKnapsack(val, wt, capacity):
    n = len(val)

    # Create list to store value and weight
    # items[i][0] = value, items[i][1] = weight
    items = [[val[i], wt[i]] for i in range(n)]

    # Sort items based on value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    res = 0.0
    currentCapacity = capacity

    # Process items in sorted order
    for i in range(n):
        # If we can take the entire item
        if items[i][1] <= currentCapacity:
            res += items[i][0]
            currentCapacity -= items[i][1]

        # Otherwise take a fraction of the item
        else:
            res += (1.0 * items[i][0] / items[i][1]) * currentCapacity

            # Knapsack is full
            break

    return res


if __name__ == "__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    capacity = 50

    print(fractionalKnapsack(val, wt, capacity))
