def get_skyline(buildings: list[list[int]]) -> list[list[int]]:
    """
    Find the skyline formed by buildings using divide and conquer.

    Args:
        buildings: List of [left, right, height] triplets

    Returns:
        List of [x, height] points defining the skyline
    """
    if not buildings:
        return []

    if len(buildings) == 1:
        left, right, height = buildings[0]
        return [[left, height], [right, 0]]

    mid = len(buildings) // 2
    left_skyline = get_skyline(buildings[:mid])
    right_skyline = get_skyline(buildings[mid:])

    return _merge_skyline(left_skyline, right_skyline)


def _merge_skyline(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    result = []
    i = j = 0
    h1 = h2 = 0
    curr_x = 0
    curr_height = 0

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            curr_x = left[i][0]
            h1 = left[i][1]
            i += 1
        elif left[i][0] > right[j][0]:
            curr_x = right[j][0]
            h2 = right[j][1]
            j += 1
        else:
            curr_x = left[i][0]
            h1 = left[i][1]
            h2 = right[j][1]
            i += 1
            j += 1

        new_height = max(h1, h2)
        if not result or result[-1][1] != new_height:
            result.append([curr_x, new_height])

    result.extend(left[i:])
    result.extend(right[j:])

    return _cleanup(result)


def _cleanup(skyline: list[list[int]]) -> list[list[int]]:
    if not skyline:
        return []

    result = [skyline[0]]
    for i in range(1, len(skyline)):
        if skyline[i][1] != result[-1][1]:
            result.append(skyline[i])

    return result


if __name__ == "__main__":
    buildings = [[1, 3, 3], [2, 4, 4], [5, 8, 2], [6, 10, 6], [9, 12, 4]]
    print(get_skyline(buildings))
