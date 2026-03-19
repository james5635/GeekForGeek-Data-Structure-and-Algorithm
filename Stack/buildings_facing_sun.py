def buildings_facing_sun(heights):
    if not heights:
        return 0
    count = 1
    max_height = heights[0]
    for i in range(1, len(heights)):
        if heights[i] > max_height:
            count += 1
            max_height = heights[i]
    return count


if __name__ == "__main__":
    h1 = [7, 4, 8, 2, 9]
    print("Heights:", h1)
    print("Buildings facing sun:", buildings_facing_sun(h1))

    h2 = [2, 3, 4, 5]
    print("\nHeights:", h2)
    print("Buildings facing sun:", buildings_facing_sun(h2))

    h3 = [6, 2, 4, 5, 1, 3]
    print("\nHeights:", h3)
    print("Buildings facing sun:", buildings_facing_sun(h3))

    h4 = [11, 13, 21, 3]
    print("\nHeights:", h4)
    print("Buildings facing sun:", buildings_facing_sun(h4))
