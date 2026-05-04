"""
Word Ladder - Shortest Transformation Sequence

Problem:
Given a start word, a target word, and a word list, find the length of the shortest
transformation sequence from start to target such that:
- Only one letter can be changed in each transformation
- Each transformed word must exist in the word list

Algorithm: BFS
- Start BFS from the start word
- For each word, try changing each character to 'a'-'z'
- If the new word is in the word list, add it to the queue
- The first time we reach the target word, return the path length

Time Complexity: O(N * M * 26) where N = number of words, M = word length
Space Complexity: O(N * M)
"""

from collections import deque


def word_ladder(start: str, target: str, word_list: list[str]) -> int:
    """
    Find the length of the shortest transformation sequence.

    Args:
        start: Starting word
        target: Target word
        word_list: List of valid words

    Returns:
        Length of shortest transformation sequence, or 0 if impossible
    """
    word_set = set(word_list)

    if target not in word_set:
        return 0

    if start == target:
        return 1

    queue = deque()
    queue.append((start, 1))
    word_set.discard(start)  # Remove start if present

    while queue:
        word, length = queue.popleft()

        # Try changing each character
        for i in range(len(word)):
            original_char = word[i]

            for c in "abcdefghijklmnopqrstuvwxyz":
                if c == original_char:
                    continue

                new_word = word[:i] + c + word[i + 1 :]

                if new_word == target:
                    return length + 1

                if new_word in word_set:
                    word_set.remove(new_word)
                    queue.append((new_word, length + 1))

    return 0


def word_ladder_with_path(
    start: str, target: str, word_list: list[str]
) -> tuple[int, list[str]]:
    """
    Find the shortest transformation sequence and return the path.

    Args:
        start: Starting word
        target: Target word
        word_list: List of valid words

    Returns:
        Tuple of (length, path) where path is the transformation sequence
    """
    word_set = set(word_list)

    if target not in word_set:
        return 0, []

    if start == target:
        return 1, [start]

    queue = deque()
    queue.append((start, [start]))
    word_set.discard(start)

    while queue:
        word, path = queue.popleft()

        for i in range(len(word)):
            original_char = word[i]

            for c in "abcdefghijklmnopqrstuvwxyz":
                if c == original_char:
                    continue

                new_word = word[:i] + c + word[i + 1 :]

                if new_word == target:
                    return len(path) + 1, path + [new_word]

                if new_word in word_set:
                    word_set.remove(new_word)
                    queue.append((new_word, path + [new_word]))

    return 0, []


if __name__ == "__main__":
    # Example 1
    word_list1 = ["des", "der", "dfr", "dgt", "dfs"]
    start1, target1 = "der", "dfs"
    length1 = word_ladder(start1, target1, word_list1)
    print(f"Example 1: '{start1}' -> '{target1}', length = {length1}")  # Output: 3

    # Example 2
    word_list2 = ["hot", "dot", "dog", "lot", "log", "cog"]
    start2, target2 = "hit", "cog"
    length2, path2 = word_ladder_with_path(start2, target2, word_list2)
    print(f"Example 2: '{start2}' -> '{target2}', length = {length2}")
    print(f"  Path: {' -> '.join(path2)}")  # Output: hit -> hot -> dot -> dog -> cog

    # Example 3
    word_list3 = ["hot", "dot", "dog", "lot", "log"]
    start3, target3 = "hit", "cog"
    length3 = word_ladder(start3, target3, word_list3)
    print(
        f"Example 3: '{start3}' -> '{target3}', length = {length3}"
    )  # Output: 0 (cog not in list)

    # Example 4
    word_list4 = ["poon", "plee", "same", "poie", "pale", "plie", "pine", "poge"]
    start4, target4 = "toon", "plea"
    length4, path4 = word_ladder_with_path(start4, target4, word_list4)
    print(f"Example 4: '{start4}' -> '{target4}', length = {length4}")
    print(f"  Path: {' -> '.join(path4)}")
