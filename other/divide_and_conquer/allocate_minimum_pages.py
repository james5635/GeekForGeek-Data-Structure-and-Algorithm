def allocate_minimum_pages(books: list[int], students: int) -> int:
    """
    Allocate books to students such that the maximum pages allocated to any student is minimized.

    Args:
        books: List of pages in each book
        students: Number of students

    Returns:
        Minimum possible value of maximum pages allocated to a student
    """
    if students > len(books):
        return -1

    low = max(books)
    high = sum(books)

    while low < high:
        mid = (low + high) // 2
        if _is_possible(books, students, mid):
            high = mid
        else:
            low = mid + 1

    return low


def _is_possible(books: list[int], students: int, max_pages: int) -> bool:
    count = 1
    current_pages = 0

    for pages in books:
        if pages > max_pages:
            return False

        if current_pages + pages > max_pages:
            count += 1
            current_pages = pages
        else:
            current_pages += pages

    return count <= students


if __name__ == "__main__":
    books = [12, 34, 67, 90]
    print(allocate_minimum_pages(books, 2))

    books2 = [10, 20, 30, 40]
    print(allocate_minimum_pages(books2, 2))
