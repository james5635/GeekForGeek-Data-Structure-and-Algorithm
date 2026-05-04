"""
Shortest Word Chain - Length of Shortest Chain to Reach Target Word

Problem:
Given an array of strings, a start word, and a target word, find the length of the
shortest chain from start to target where:
- Adjacent words in the chain differ by exactly one character
- Each word in the chain must exist in the given array

This is similar to Word Ladder but may have different input format.

Algorithm: BFS
- Use a set for O(1) word lookups
- From each word, generate all words that differ by one character
- BFS guarantees finding the shortest chain

Time Complexity: O(N * M * 26) where N = number of words, M = word length
Space Complexity: O(N * M)
"""

from collections import deque


def shortest_word_chain(start: str, target: str, word_list: list[str]) -> int:
    """
    Find the length of the shortest chain from start to target.

    Args:
        start: Starting word
        target: Target word
        word_list: List of valid words in the dictionary

    Returns:
        Length of shortest chain, or 0 if no chain exists
    """
    word_set = set(word_list)

    if target not in word_set:
        return 0

    if start == target:
        return 1

    # Use BFS
    queue = deque()
    queue.append(start)
    word_set.discard(start)
    chain_length = 1

    while queue:
        chain_length += 1
        level_size = len(queue)

        for _ in range(level_size):
            word = queue.popleft()

            # Try changing each character
            for i in range(len(word)):
                original_char = word[i]

                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == original_char:
                        continue

                    new_word = word[:i] + c + word[i + 1 :]

                    if new_word == target:
                        return chain_length

                    if new_word in word_set:
                        word_set.remove(new_word)
                        queue.append(new_word)

    return 0


def shortest_word_chain_with_path(
    start: str, target: str, word_list: list[str]
) -> tuple[int, list[str]]:
    """
    Find the shortest chain and return the actual path.

    Args:
        start: Starting word
        target: Target word
        word_list: List of valid words

    Returns:
        Tuple of (length, path) where path is the word sequence
    """
    word_set = set(word_list)

    if target not in word_set:
        return 0, []

    if start == target:
        return 1, [start]

    queue = deque()
    queue.append([start])
    word_set.discard(start)

    while queue:
        path = queue.popleft()
        word = path[-1]

        for i in range(len(word)):
            original_char = word[i]

            for c in "abcdefghijklmnopqrstuvwxyz":
                if c == original_char:
                    continue

                new_word = word[:i] + c + word[i + 1 :]

                if new_word == target:
                    new_path = path + [new_word]
                    return len(new_path), new_path

                if new_word in word_set:
                    word_set.remove(new_word)
                    queue.append(path + [new_word])

    return 0, []


def are_adjacent(word1: str, word2: str) -> bool:
    """Check if two words differ by exactly one character."""
    if len(word1) != len(word2):
        return False
    diff_count = sum(1 for a, b in zip(word1, word2) if a != b)
    return diff_count == 1


if __name__ == "__main__":
    # Example 1
    word_list1 = ["des", "der", "dfr", "dgt", "dfs"]
    start1, target1 = "der", "dfs"
    length1 = shortest_word_chain(start1, target1, word_list1)
    print(f"Example 1: '{start1}' -> '{target1}', length = {length1}")  # Output: 3

    # Example 2
    word_list2 = ["poon", "plee", "same", "poie", "pale", "plie", "pine", "poge"]
    start2, target2 = "toon", "plea"
    length2, path2 = shortest_word_chain_with_path(start2, target2, word_list2)
    print(f"Example 2: '{start2}' -> '{target2}', length = {length2}")
    if path2:
        print(f"  Path: {' -> '.join(path2)}")

    # Example 3
    word_list3 = ["cat", "bat", "bet", "bed", "dat", "dag", "dog"]
    start3, target3 = "cat", "dog"
    length3, path3 = shortest_word_chain_with_path(start3, target3, word_list3)
    print(f"Example 3: '{start3}' -> '{target3}', length = {length3}")
    if path3:
        print(f"  Path: {' -> '.join(path3)}")

    # Example 4: No chain possible
    word_list4 = ["cat", "bat", "rat"]
    start4, target4 = "cat", "dog"
    length4 = shortest_word_chain(start4, target4, word_list4)
    print(f"Example 4: '{start4}' -> '{target4}', length = {length4}")  # Output: 0

    # Example 5: Adjacency check
    print(f"\nAdjacency check: 'cat' and 'bat': {are_adjacent('cat', 'bat')}")  # True
    print(f"Adjacency check: 'cat' and 'dog': {are_adjacent('cat', 'dog')}")  # False
